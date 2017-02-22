import utilities.geoCalc as geo
from utilities.converters import metricImperial

from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as func

def geoEncode(spark):
    # read the data in
    uber = spark.read.csv(
        'uber_data_nyc_2016-06_3m_partitioned.csv', 
        header=True, 
        inferSchema=True
        )\
        .repartition(4) \
        # .select('VendorID','tpep_pickup_datetime', 'pickup_longitude', 'pickup_latitude','dropoff_longitude','dropoff_latitude','total_amount')

    # prepare the UDFs
    getDistance = func.udf(
        lambda lat1, long1, lat2, long2: 
            geo.calculateDistance(
                (lat1, long1),
                (lat2, long2)
            )
        )

    convertMiles = func.udf(lambda m: 
        metricImperial.convert(str(m) + ' mile', 'km'))

    # create new columns
    uber = uber.withColumn(
        'miles', 
            getDistance(
                func.col('pickup_latitude'),
                func.col('pickup_longitude'), 
                func.col('dropoff_latitude'), 
                func.col('dropoff_longitude')
            )
        )

    uber = uber.withColumn(
        'kilometers', 
        convertMiles(func.col('miles')))

    # print 10 rows
    # uber.show(10)

    # save to csv (partitioned)
    uber.write.csv(
        'uber_data_nyc_2016-06_new.csv',
        mode='overwrite',
        header=True,
        compression='gzip'
    )

if __name__ == '__main__':
    spark = SparkSession \
        .builder \
        .appName('CalculatingGeoDistances') \
        .getOrCreate()

    print('Session created')

    try:
        geoEncode(spark)

    finally:
        spark.stop()
#
# Streaming Word Count Example
#    Original Source: https://spark.apache.org/docs/1.6.0/streaming-programming-guide.html
#
# To run this example:
#   Terminal 1:  nc -lk 9999
#	Terminal 2:  ./bin/spark-submit streaming_word_count.py localhost 9999
#   Note, type words into Terminal 1
#

# Import the necessary classes and create a local SparkContext and Streaming Contexts
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create Spark Context with two working threads (note, `local[2]`)
sc = SparkContext("local[2]", "NetworkWordCount")

# Create local StreamingContextwith batch interval of 1 second
ssc = StreamingContext(sc, 1)

# Create DStream that will connect to the stream of input lines from connection to localhost:9999
lines = ssc.socketTextStream("localhost", 9999)

# Split lines into words
words = lines.flatMap(lambda line: line.split(" "))

# Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

# Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.pprint()

# Start the computation
ssc.start()             

# Wait for the computation to terminate
ssc.awaitTermination()  


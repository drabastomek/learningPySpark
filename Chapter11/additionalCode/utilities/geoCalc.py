import math

class geoCalc(object):
    @staticmethod
    def calculateDistance(p1, p2):
        '''
            calculates the distance using Haversine formula
        '''
        R = 3959 # earth's radius in miles

        # get the coordinates
        lat1, lon1 = p1[0], p1[1]
        lat2, lon2 = p2[0], p2[1]

        # convert to radians
        deltaLat_radians = math.radians(lat2-lat1)
        deltaLon_radians = math.radians(lon2-lon1)

        lat1_radians = math.radians(lat1)
        lat2_radians = math.radians(lat2)

        # apply the formula
        hav = math.sin(deltaLat_radians / 2.0) * \
            math.sin(deltaLat_radians / 2.0) + \
            math.sin(deltaLon_radians / 2.0) * \
            math.sin(deltaLon_radians / 2.0) * \
            math.cos(lat1_radians) * \
            math.cos(lat2_radians) 

        dist = 2 * R * math.asin(math.sqrt(hav)) 

        return dist

if __name__ == '__main__':
    p1 = {'address': '301 S Jackson St, Seattle, WA 98104',
    'lat': 47.599200, 
    'long': -122.329841}

    p2 = {'address': 'Thunderbird Films Inc 533, Smithe St #401, Vancouver, BC V6B 6H1, Canada',
        'lat': 49.279688, 
        'long': -123.119190}

    print(geoCalc.calculateDistance((p1['lat'], p1['long']), (p2['lat'], p2['long'])))
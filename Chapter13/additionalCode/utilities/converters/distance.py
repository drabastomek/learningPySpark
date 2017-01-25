from ..base import BaseConverter

class metricImperial(BaseConverter):
    pass

    @staticmethod
    def convert(f, t):
        conversionTable = {
            'in': {  
                'mm': 25.4,    'cm': 2.54,     'm': 0.0254, 
                'km': 0.0000254
            }, 'ft': {  
                'mm': 304.8,   'cm': 30.48,    'm': 0.3048,
                'km': 0.0003048
            }, 'yd': {  
                'mm': 914.4,   'cm': 91.44,    'm': 0.9144,
                'km': 0.0009144
            }, 'mile': {    
                'mm': 1609344, 'cm': 160934.4, 'm': 1609.344,
                'km': 1.609344
            }   
        }

        f_val, f_unit = f.split(' ')
        f_val = float(f_val)

        if f_unit in conversionTable.keys():
            if t in conversionTable[f_unit].keys():
                conv = 1 / conversionTable[f_unit][t]
            else:
                raise KeyError('Key {0} not found...' \
                    .format(t))
        elif t in conversionTable.keys():
            if f_unit in conversionTable[t].keys():
                conv = conversionTable[t][f_unit]
            else:
                raise KeyError('Key {0} not found...' \
                    .format(f_unit))
        else:
            raise KeyError('Neither {0} nor {1} key found'\
                .format(t, f_unit))

        return f_val / conv

if __name__ == '__main__':
    f = metricImperial()
    print(f.convert('10 mile', 'km'))
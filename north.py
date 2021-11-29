# Correct

import sys

dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']

for line in sys.stdin:
    line = line.rstrip('\n')

    try:
        i = dirs.index(line)
        print(line + " is " + str(i * (180 / 8)) + " degrees")
    except ValueError:
        pass

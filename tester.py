import sys
import geo.utils as utils

line_raw = sys.stdin.readline()

if line_raw:
    parts = line_raw.split()

    if len(parts) == 3:
        a = int(parts[0])
        b = int(parts[1])
        r = int(parts[2])

        c = utils.pythagoras(a, b)
        print('c', c)

        area = utils.circle(r)
        print('area =', area)

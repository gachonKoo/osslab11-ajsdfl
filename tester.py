import sys
import geo.utils as utils

line_raw = sys.stdin.readline()

if line_raw:
    parts = line_raw.split()
    
    if len(parts) == 2:
        a = int(parts[0])
        b = int(parts[1])
        c = utils.pythagoras(a, b)
        print('c', c)
        
    elif len(parts) == 1:
        r = int(parts[0])
        area = utils.circle(r)
        print('area =', area)

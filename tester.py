import sys
import geo.utils as utils

line1_raw = sys.stdin.readline() 

if line1_raw and len(line1_raw.split()) >= 2:
    line1_parts = line1_raw.split()
    a = int(line1_parts[0])
    b = int(line1_parts[1])
    
    line2_raw = sys.stdin.readline()
    
    if line2_raw and len(line2_raw.split()) >= 1:
        line2_parts = line2_raw.split()
        r = int(line2_parts[0])

        c = utils.pythagoras(a, b)
        print('c', c)
        
        area = utils.circle(r)
        print('area =', area)

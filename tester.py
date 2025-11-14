# tester.py
import sys
import geo.utils as utils

line1_raw = sys.stdin.readline()

if line1_raw:
    parts1 = line1_raw.split()
    
    if len(parts1) == 3:
        a = int(parts1[0])
        b = int(parts1[1])
        r = int(parts1[2])
    
        c = utils.pythagoras(a, b)
        print('c', c)
        
        area = utils.circle(r)
        print('area =', area)

    elif len(parts1) == 2:
        a = int(parts1[0])
        b = int(parts1[1])

        line2_raw = sys.stdin.readline()
        
        if line2_raw:
            parts2 = line2_raw.split()
            if len(parts2) == 1:
                r = int(parts2[0])
                
                c = utils.pythagoras(a, b)
                print('c', c)
                
                area = utils.circle(r)
                print('area =', area)

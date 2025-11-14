# tester.py
import sys
import geo.utils as utils

# --- 1. a와 b 값 읽어오기 ---
line1_raw = sys.stdin.readline() 

# line1_raw가 비어있지 않은지 확인 (오류 방지)
if line1_raw and len(line1_raw.split()) >= 2:
    line1_parts = line1_raw.split()
    a = int(line1_parts[0])
    b = int(line1_parts[1])
    
    # --- 2. r 값 읽어오기 ---
    line2_raw = sys.stdin.readline()
    
    # line2_raw가 비어있지 않은지 확인 (오류 방지)
    if line2_raw and len(line2_raw.split()) >= 1:
        line2_parts = line2_raw.split()
        r = int(line2_parts[0])

        # --- 3. 두 값이 모두 정상일 때, 두 개의 결과를 모두 출력 ---
        c = utils.pythagoras(a, b)
        print('c', c)
        
        area = utils.circle(r)
        print('area =', area)

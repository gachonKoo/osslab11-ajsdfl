# geo/utils.py
import math

def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def circle(r):
    # 이 부분이 r ** 2 (제곱) 이어야 합니다.
    area = math.pi * r ** 2
    return area

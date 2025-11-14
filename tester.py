
import geo.utils as utils
import sys

line1 = sys.stdin.readline().split()
a = int(line1[0])
b = int(line1[1])

line2 = sys.stdin.readline().split()
r = int(line2[0])

c = utils.pythagoras(a, b)
print('c', c)

area = utils.circle(r)
print('area =', area)

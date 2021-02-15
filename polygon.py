import math
def polysum(n,s):
    area = (0.25*(n*(s**2)))/ math.tan(math.pi/n)
    perimeter = (n*s)
    print(area + (perimeter**2))
polysum(4,2)
# This function accept the radius of a circle and calculates the area
# #math lib is used to calculated area
import math
def getradius():
    r = float(input('Enter the radius :'))
    area = (math.pi * (r * r))
    print(f'Radius: {r} \nArea of the circle: {area:.2f}')

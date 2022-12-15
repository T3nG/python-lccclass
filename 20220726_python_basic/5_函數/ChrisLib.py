import math

    # Temperature transfer

# Celsius to Fahrenheit
def cel2fah(c):
    f=c*9/5+32
    return f

# Fahrenheit to Celsius
def fah2cel(f):
    c=(f-32)*5/9
    return c

    # Geometry

# Radian to Degree
def rad2deg(r):
    d=r*180/math.pi
    return d

# Degree to Radian
def deg2rad(d):
    r=d*math.pi/180
    return r

    # Trigonometry
'''
sin()=opposite/hypotenuse
cos()=adjacent/hypotenuse
tan()=opposite/adjacent=sin()/cos()
soh cah toa

    unit circle
(sin())^2+(cos())^2=1


Angle   cos         sin         tan
30 d    (3^0.5)/2   1/2         (3^0.5)/3
45 d    (2^0.5)/2   (2^0.5)/2   1
60 d    1/2         (3^0.5)/2   3^0.5

secant    = 1/cos
cosecant  = 1/sin
cotangent = 1/tan
'''

    # Unit Circle
# radius, degree
def circle(r,d):
    x = r * math.cos(deg2rad(d))
    y = r * math.sin(deg2rad(d))
    return x,y

#math library dependency has to be imported first
import math

# A regular polygon has 'n' number of sides. Each side has length 's'.
# * The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
# * The perimeter of a polygon is: length of the boundary of the polygon

def polysum(n, s):
    '''
    #     n: (int or float) number of sides of a polygon
    #     a: (int or float )length of each side
    #
    #     returns: the sum of the area and square of the perimeter of the regular polygon
    #     '''
    polygonarea = (0.25*n*(s*s))/(math.tan(math.pi/n))
    polygonperimeter = s*n
    return round(polygonarea + (polygonperimeter * polygonperimeter),4)

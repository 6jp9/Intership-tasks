# # to check whether a point inside the triangle area or not
# # point
# x = (2,2)
# # Triangle
# p1=(2,3)
# p2=(1,1)
# p3=(3,1)

# def test(p=(),q=(),r=(),x=()):
#     def area(a,b,c):
#         area1=abs(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1]))/2
#         return area1
#     if area(p,q,r) == area(p,q,x)+area(q,r,x)+area(p,r,x) :
#         return 'point is inside the triangle!!'
#     return 'point is outside the triangle!!'

# print(test(p1,p2,p3,x))

###########################################################################
# to determine whether the two rectangles are intersecting or not
#rectangle 1

# p=(1,5)
# q=(5,1)
# #rectangle 2
# r=(-1,7)
# s=(2,6)
# def test(p,q,r,s):
#     if ((r[0] in range(min(q[0],p[0]),max(q[0],p[0])+1)) and (r[1] in range(min(q[1],p[1]),max(q[1],p[1])+1))) or ((s[0] in range(min(q[0],p[0]),max(q[0],p[0])+1)) and (s[1] in range(min(q[1],p[1]),max(q[1],p[1])+1))):
#         return True
#     return False
# if test(p,q,r,s):
#     print('rectangles are intersecting')
# else:
#     print('rectangles are not intersecting')

#############################################################################
# To find the minimal point of a rectangle to the center of the circle

# import math
# center = (1,2)
# p=(1,5)
# q=(1,2)
# r=(5,1)
# s=(5,5)

# lst=[p,q,r,s]
# def test(lst,center,i=0,lst1=[],dict1={}):
#     def distance(x,y):
#         d = math.sqrt(((y[0]-x[0])**2)+((y[1]-x[1])**2))
#         print(d)
#         return d
#     if i<len(lst):
#         lst1.append(distance(lst[i],center))
#         print(lst1)
#         dict1[distance(lst[i],center)]=lst[i]
#         print(dict1)
#         return test(lst,center,i+1,lst1,dict1)
#     return dict1.get(min(lst1)),'is the minimal point'

# print(test(lst,center))

############################################################################

import math
r1=5
r2=7
c1=(1,1)
c2=(6,6)

def area_of_intersected(r1,r2,c1,c2):
    d=math.sqrt(((c1[0]-c2[0])**2) + (c1[1]-c2[1])**2 )
    if d>=r1+r2:
        return 0
    elif d<=abs(r1-r2):
        return (math.pi)*(min(r1,r2))**2
    else:
        area = r1**2 * (math.acos((d**2+r1**2-r2**2)/(2*d*r1))) + r2**2 * (math.acos((d**2+r2**2-r1**2)/(2*d*r2))) - (1/2) * math.sqrt((d+r1+r2)*(d+r1-r2)*(d+r2-r1)*(r1+r2-d))
        return area
    
print('area of the intersected part:',area_of_intersected(r1,r2,c1,c2))


############################################################################




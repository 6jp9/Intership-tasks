# to determine whether the two rectangles are intersecting or not
# rectangle 1
# r1=[0,0,1,1]

# p=(r1[0],r1[1])
# q=(r1[2],r1[3])
# #rectangle 2
# r2=[1,1,3,3]

# r=(r2[0],r2[1])
# s=(r2[2],r2[3])
# def test(p,q,r,s):
#     if ((r[0] in range(min(q[0],p[0]),max(q[0],p[0])+1)) and (r[1] in range(min(q[1],p[1]),max(q[1],p[1])+1))) or ((s[0] in range(min(q[0],p[0]),max(q[0],p[0])+1)) and (s[1] in range(min(q[1],p[1]),max(q[1],p[1])+1))):
#         return True
#     return False
# if test(p,q,r,s):
#     print('rectangles are intersecting')
# else:
#     print('rectangles are not intersecting')

##################################################################


# def test(lst, n, target, i=0):
#     if i + n > len(lst):
#         return None
#     slice = lst[i:i+n]
#     if sum(slice) == target:
#         return slice
#     return test(lst, n, target, i + 1)

# lst = [10, 20, 30, 40, 50, 60, 70, 90]
# n = 2
# target = 150
# result = test(lst, n, target)
# print(result)


###################################################################

# lst = [1,2,1,2,3,0,0,0,4,0,3,0]
# pos=0
# for i in range(len(lst)):
#     if lst[i]!=0:
#         lst[i],lst[pos]=lst[pos],lst[i]
#         pos+=1
# print(lst)

# ###################################################################

# import math
# dict1 = {'df': {'A':[4, 16, 25, 36], 'B': [1, 4, 9, 10]}}
# for _,data in dict1.items():
#     for _ in range(len(data['A'])):
#         a=data['A'][0]
#         b=data['B'][0]
#         data['A'].remove(a)
#         data['A'].append(math.sqrt(a))
#         data['B'].remove(b)
#         data['B'].append(math.sqrt(b))
# print(dict1)

###################################################################

# lst = [7,3,8,-1,4,0,5]
# n= len(lst)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if lst[j]>lst[j+1]:
#             lst[j],lst[j+1]=lst[j+1],lst[j]
# print(lst)
# mid = int(len(lst)/2)
# if len(lst)%2==0:
#     median = (lst[mid]+lst[mid-1])/2
#     print(median)
# else:
#     median=lst[mid]
#     print(median)

###################################################################


# string = 'aabbabaccdcddababad'
# lst = []
# def pal(string,lst=lst,n=1):
#     if n<len(string):
#         for i in range(len(string)):
#             sub = string[i:i+n]
#             if sub==sub[::-1]:
#                 lst.append(sub)
#         return pal(string,lst,n+1)
#     lst1=list(set(lst))
#     def dic(lst=lst1,dict1={},s=1):
#         temp = []
#         if s<len(lst1):
#             for i in lst1:
#                 if len(i)==s:
#                     temp.append(i)
#             if len(temp)>0:
#                 dict1[s]=temp
#             return dic(lst,dict1,s+1)
#         return dict1
#     return dic()
# print(pal(string))


# ###################################################################

def intersection_area(rect1, rect2):
    p1, q1, r1, s1 = rect1
    p2, q2, r2, s2 = rect2
    print( p1, q1, r1, s1)
    print(p2, q2, r2, s2)

    p = max(p1, p2)
    q = max(q1, q2)
    r = min(r1, r2)
    s = min(s1, s2)
    print(p,r,q,s)

    if r > p and s > q:
        area = (r - p) * (s - q)
        return area
    else:
        return 'Rectangles are not intersected'

rect1 = (1, 1, 5, 5)
rect2 = (3, 2, 6, 4)

area = intersection_area(rect1, rect2)
print(f"The area of the intersection is: {area}")



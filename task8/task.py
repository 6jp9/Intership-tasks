

# string = 'aaaabbbbbbcccccccd'
# i,j=0,1
# result=''
# while j<=len(string):
#     if j<len(string) and string[i]==string[j]:
#         j+=1
#     else:
#         result+=string[i]+str(len(string[i:j]))
#         i,j=j,j+1
# print(result)



#################################################



# string = 'aaaaxbbbbbbcccccccd'
# i,j=0,1
# result=''
# while j<=len(string):
#     if j<len(string) and string[i]==string[j]:
#         j+=1
#     else:
#         if len(string[i:j])!=1:
#             result+=string[i]+str(len(string[i:j]))
#         else:
#             result+=string[i]
#         i,j=j,j+1
# print(result)



##################################################



# import math
# lst=[[2,3],[2,-2],[3,-4]]
# k=2
# sqrs=[]
# for i in lst:
#     x=0
#     for j in i:
#         x+=j**2
#     sqrs.append((math.sqrt(x),i))

# for i in range(k):
#     near=min(sqrs)
#     print(near)
#     sqrs.remove(near)



####################################################



# lst=[2,3,-4,15,11,-9,-17,11,34,-19]
# lst1=lst
# k=4
# def k_smallest_elements(lst1,k,lst2=[]):
#     if k!=0:
#         temp = lst[0]
#         for i in lst:
#             if temp>i:
#                 temp=i
#         lst2.append(temp)
#         lst1.remove(temp)
#         return k_smallest_elements(lst1,k-1,lst2)
#     return lst2
        
# print(k_smallest_elements(lst1,k))



#####################################################



string = 'booom'
invert = string[::-1]
if string==string[::-1]:
    print('-----------------------------------')
    print(f'the given string {string} is a palindrome')
    print('-----------------------------------')

elif string[-1]!=string[-2]:
    print('-----------------------------------')
    print(string+invert[1:])
    print('-----------------------------------')
else:
    i,j=0,1
    while True:
        if j<len(invert) and invert[i]==invert[j]:
            j+=1
        else:
            temp=len(invert[i:j])
            result= string+invert[temp:]
            break
    print('-----------------------------------')
    print(result)
    print('-----------------------------------')

dict1={1:'m1',2:'m2',3:'m3',4:'m4'}

lst=[2,3,4,1]

print(dict1)
def insert(dict1,item,lst=lst):
    lru = lst[0]
    dict1[lru]=item
    lst.remove(lru)
    lst.append(lru)
    return dict1

print(insert(dict1,'m5'))


# for i in range(15):
#     print(insert(dict1,i))


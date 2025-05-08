
import math
dict1 = {'df': {'A':[4, 16, 25, 36], 'B': [1, 4, 9, 16]}}
for _,data in dict1.items():
    for _ in range(len(data['A'])):
        a=data['A'][0]
        b=data['B'][0]
        print(a,b)
        data['A'].remove(a)
        data['A'].append(int(math.sqrt(a)))
        data['B'].remove(b)
        data['B'].append(int(math.sqrt(b)))
print(dict1)

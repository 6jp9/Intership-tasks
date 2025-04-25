
lst = [5,3,6,9,10]
def last_square(lst,start=0,last=len(lst)-1):
    while start!=last:
        if lst[start]>lst[last]:
            start+=1
        else:
            last-=1
        return last_square(lst,start,last)
    return lst[start]
# print(last_square(lst))

#########################################


n=3
profit = [25,24,15]
weight = [18,15,10]
bag = 20
def high_profit(profit,weight,bag,n,ratio=[]):
    for i in range(n):
        ratio.append(profit[i]/weight[i])
    total = 0
    while bag>0:

        max_ratio = max(ratio)
        index = ratio.index(max_ratio)
        if weight[index] <= bag:
            total += profit[index]
            bag -= weight[index]
        else:
            total += max_ratio * bag
            bag = 0
        ratio[index] = 0
        
    return total
# print(high_profit(profit,weight,bag,n))

#############################################

def max_friends(days):
    return len(set(days))
days=[3,3,1,2,4]
# print(max_friends(days))

#############################################

arr = [1, 2, 3, 4, 5, 6, 0]

def max_product(arr):
    prod = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                prod.append(arr[i] * arr[j])
    return max(prod)

# print(max_product(arr))

#############################################


        



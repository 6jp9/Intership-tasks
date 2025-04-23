
################################
#queue

class Queue:
    def __init__(self):
        self.que = []
    def insert(self,item):
        self.que.append(item)
        print(self.que)
    def remove(self):
        self.que.pop(0)
        print(self.que)
    def front(self):
        if self.isempty():
            print('queue is empty!')
        else:
            print(self.que[0])
    def end(self):
        if self.isempty():
            print('queue is empty!')
        else:
            print(self.que[-1])
    def isempty(self):
        if len(self.que)==0:
            return True
        return False

# s=Queue()
# s.insert(10)
# s.remove()
# print(s.isempty())
# s.front()
# s.end()

#############################
#Binary search tree

class BinarySearchTree():
    def __init__(self):
        self.tree = []

    def insert(self, item, tree=None):
        if tree is None:
            tree = self.tree

        if tree == []:
            tree += [item, [], []]
        elif item < tree[0]:
            tree[1] = self.insert(item, tree[1])
        elif item > tree[0]:
            tree[2] = self.insert(item, tree[2])
        return tree
    
    def search(self,item,tree):
        if tree == []:
            return False
        elif tree[0]==item:
            return True
        elif item<tree[0]:
            return self.search(item,tree[1])
        elif item>tree[0]:
            return self.search(item,tree[2])
        


    def display(self):
        print(self.tree)


tree = BinarySearchTree()
n=int(input('number of nodes:'))
c=1
while c<=n:
    item=int(input('enter item:'))
    tree.insert(item)
    c+=1
tree.display()
print(tree.search(6,tree.tree))



##########################################
#Largest and non duplicate sub string

def lss(string, i=0, lst=None):
    if lst is None:
        lst = []
    if i>=len(string):
        return lst
    sub = ''
    while i < len(string) and string[i] not in sub:
        sub += string[i]
        i += 1
    lst.append(sub)
    return lss(string,i+1,lst)

# string = 'abababasadsadsaaaassadfedsc'
# a=lss(string)
# # print(a)
# large_sub_string=''
# for i in a:
#     if len(i)>len(large_sub_string):
#         large_sub_string=i
# print('Largest and non duplicate sub string in',string,'is',large_sub_string)


################################

s='ababababababaabbjpcc'
pattern = 'jp'
def patt(string,pattern):
    front = 0
    end=len(pattern)
    while end<=len(string):
        sub=string[front:end]
        if sub==pattern:
            return f'match found at {front} to {end}'
        else:
            front+=1
            end+=1
    return 'match not found'
#print(patt(s,pattern))


# words = [
#     'apple', 'banana', 'grape', 'orange', 'mango', 'peach', 'cherry', 'lemon', 'melon', 'plum',
#     'carrot', 'onion', 'tomato', 'potato', 'cabbage', 'celery', 'spinach', 'pepper', 'garlic', 'radish',
#     'table', 'chair', 'sofa', 'bed', 'shelf', 'lamp', 'mirror', 'window', 'curtain', 'pillow',
#     'river', 'mountain', 'valley', 'desert', 'ocean', 'island', 'forest', 'hill', 'lake', 'cave',
#     'happy', 'sad', 'angry', 'excited', 'nervous', 'calm', 'bored', 'tired', 'brave', 'shy',
#     'run', 'walk', 'jump', 'sleep', 'eat', 'drink', 'read', 'write', 'draw', 'cook',
#     'cat', 'dog', 'mouse', 'horse', 'sheep', 'goat', 'lion', 'tiger', 'zebra', 'bear',
#     'cloud', 'rain', 'snow', 'storm', 'wind', 'sun', 'fog', 'thunder', 'lightning', 'breeze',
#     'book', 'pen', 'paper', 'bag', 'box', 'key', 'phone', 'watch', 'clock', 'coin',
#     'blue', 'green', 'red', 'yellow', 'purple', 'white', 'black', 'gray', 'pink', 'brown'
# ]



# def auto_completion(words=words):
    
#     inp = input('enter a prefix or string to search:')
#     lst = []

#     for word in words:
#         if word.startswith(inp.lower()):
#             lst.append(word)
#     if lst:
#         print(lst)
#         matches = len(lst)
#         return f'{matches} matches found!!'
        
#     return 'No matches Found!!'

# def insert_word(words=words):
#     inp = input('enter a prefix or string to insert:')
#     if inp not in words:
#        words.append(inp)
#     return 'Done!!'
# def delete_word(words=words):
#     inp = input('enter a prefix or string to delete:')
#     if inp in words:
#         words.remove(inp)
#     return 'Done!!'


# print('1.search\n2.insert\n3.delete\n4.list\nexit')
# while True:
#     x = int(input('enter a choice:'))
#     if x==1:
#         print(auto_completion())
#     elif x==2:
#         print(insert_word())
#     elif x==3:
#         print(delete_word())
#     elif x==4:
#         print(words)
#     else:
#         break




#######################################################################################################
# dict1={}
# n=97
# while n<=122:
#     pre = chr(n)
#     ls = []
#     for word in words:
#         if word.lower().startswith(pre):
#             ls.append(word)
#     dict1[pre] = ls
#     n+=1

# print(dict1)


words = {'a': ['apple', 'angry'], 
 'b': ['banana', 'bed', 'bored', 'brave', 'bear', 'breeze', 'book', 'bag', 'box', 'blue', 'black', 'brown'], 
 'c': ['cherry', 'carrot', 'cabbage', 'celery', 'chair', 'curtain', 'cave', 'calm', 'cook', 'cat', 'cloud', 'clock', 'coin'], 
 'd': ['desert', 'drink', 'draw', 'dog'], 
 'e': ['excited', 'eat'], 
 'f': ['forest', 'fog'], 
 'g': ['grape', 'garlic', 'goat', 'green', 'gray'], 
 'h': ['hill', 'happy', 'horse'], 
 'i': ['island'], 
 'j': ['jump'], 
 'k': ['key'], 
 'l': ['lemon', 'lamp', 'lake', 'lion', 'lightning'], 
 'm': ['mango', 'melon', 'mirror', 'mountain', 'mouse'], 
 'n': ['nervous'], 
 'o': ['orange', 'onion', 'ocean'], 
 'p': ['peach', 'plum', 'potato', 'pepper', 'pillow', 'pen', 'paper', 'phone', 'purple', 'pink'], 
 'q': [], 
 'r': ['radish', 'river', 'run', 'read', 'rain', 'red'], 
 's': ['spinach', 'sofa', 'shelf', 'sad', 'shy', 'sleep', 'sheep', 'snow', 'storm', 'sun'], 
 't': ['tomato', 'table', 'tired', 'tiger', 'thunder'], 
 'u': [], 
 'v': ['valley'], 
 'w': ['window', 'walk', 'write', 'wind', 'watch', 'white'], 
 'x': [], 
 'y': ['yellow'], 
 'z': ['zebra']}
    
 
def auto_completion(words=words):
    
    inp = input('enter a prefix or string to search:')
    lst = []
    pre = inp[0]
    for word in words[pre.lower()]:
        if word.startswith(inp.lower()):
            lst.append(word)   
    if lst:
        print(lst)
        matches = len(lst)
        return f'{matches} matches found!!'
    return 'No matches Found!!'


def insert_word(words=words):
    inp = input('enter a prefix or string to insert:')
    pre = inp[0]
    if inp not in words[pre.lower()]:
       words[pre.lower()].append(inp)
    return 'Done!!'

def delete_word(words=words):
    inp = input('enter a string to delete:')
    pre = inp[0]
    if inp in words[pre.lower()]:
        words[pre.lower()].remove(inp)
        return 'Done!!'
    return 'enter the complete word!! or string does not exist!!'

print('1.search\n2.insert\n3.delete\n4.list\nexit')
while True:
    x = int(input('enter a choice:'))
    if x==1:
        print(auto_completion())
    elif x==2:
        print(insert_word())
    elif x==3:
        print(delete_word())
    elif x==4:
        print(words)
    else:
        break

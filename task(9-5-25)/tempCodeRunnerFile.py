
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



book={}
def view_contacts():
    if book!={}:
        for key,value in book.items():
            print(f'{key}:{value}')
    else:
        print('No contacts!!')

def create_contact(name,number):
    book[name]=number
    
    return book

def search_contact(name=None):
    if name!=None:
        c=0
        for key,value in book.items():
            # if key.lower() == name.lower() or value == number:
            if key.startswith(str(name)):
                print(f'{key}:{value}')
                c+=1
        return f'{c} contacts found!'
        
    return 'Contact does not exist!!!'

def delete_contact(name=None,number=None):
    delete=None
    if name!=None or number!=None:
        for key,value in book.items():
            if key.lower() == name.lower() or value == number:
                delete = key
        if delete:
            del book[key]
            return 'contact deleted!!'
    return 'Contact does not exist!!!'

while True:
    print('1.view Contacts\n2.add contact\n3.search contact\n4.delete contact')
    try:
        inp = int(input('choose an operation:'))
    except ValueError:
        print("Please enter a valid operation!")
        break

    if inp==2:
        try:
            name = input('enter contact name:')
            number = int(input('enter contact number:'))
            print(create_contact(name,number))
        except:
            print('invalid Name or Number!!!')
    elif inp==1:
        view_contacts()
    elif inp==3:
        se= input('search contact name:')
        print(search_contact(se))
    elif inp==4:
        view_contacts()
        name = input('name:')
        print(search_contact(name))
        ans=input('are you sure that you want to delete this contact?[Y|N]')
        if ans.lower()=='y':
            print(delete_contact(name))
        else:
            print('canceled!!')
    else:
        print('invalid operation!!! exiting!!')
        break



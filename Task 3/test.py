import os,re

file_name = 'sample.txt'

def FileHandling():
    print('*************\n1. Create\n2. Read\n3. Content Modification\n4. Remove Content\n5. Rename\n6. Add Content\n7. Search\n8. Close')
    n = int(input('choose an operation:'))
    if n==1:
        text = 'sample text'
        with open(file_name,'w') as file:
            file.write(text)
        print('file created!!')
    elif n==2:
        try:
            with open(file_name,'r') as file:
                for txt in file:
                    print('--------------')
                    print(txt.strip())
        except FileNotFoundError:
            print('file not found!!')
    elif n==3:
        try:
            with open(file_name,'r') as file:
                text=file.read()
                text=text.replace('text','message')
            with open(file_name,'w') as file:
                file.write(text)
            print('text modified!')
        except:
            print('file not found!!')
    elif n==4:
        try:
            with open(file_name,'r') as file:
                text=file.read()
                text=text.replace('jp','')
            with open(file_name,'w') as file:
                file.write(text)
            print('text removed!')
        except:
            print('file not found!!')
    elif n==5:
        try:
            os.rename(file_name,'dirt.txt')
            print('rename done!!')
        except:
            print('file not found!! or file already existed!!')
    elif n==6:
        try:
            with open(file_name,'a') as file:
                text = '\nGood morning!'
                file.write(text)
            print('Text added!!')
        except:
            print('file not found!!')
    elif n==7:
        try:
            with open(file_name,'r') as file:
                data = file.read()
                pattern = r'hello'
                match = re.findall(pattern, data)
                if match:
                    print("Search is found:", match)
                else:
                    print("Search is not found")
        except:
            print("File not found")
    elif n==8:
        with open(file_name,'r') as file:
            print(file.read())
        print('file closed??..',file.closed)
    else:
        print('enter a valid choice!!!')
        x=input('would like to retry?[Y or N]:')
        if x.lower()=='y':
            FileHandling()
        else:
            print('End!!')
FileHandling()
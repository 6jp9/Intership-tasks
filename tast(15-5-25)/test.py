from pypdf import PdfReader
import re 
file_path = r"C:\Users\LENOVO\OneDrive\Desktop\Fullstack\Backend\python\Internship\outcome.pdf"
with open(file_path,mode='rb') as f:
    r = PdfReader(f)
    text=''
    for i in r.pages:
        text += i.extract_text()

pattern = r"(?i)(total\s+due|sub\s*total|total)\s*((?:\$\d+(?:\.\d+)?|\d+(?:\.\d+)?€))"

all_amounts = re.findall(pattern, text)
for i in all_amounts:
    print(i[0],':',i[1])





# lst = all_amounts[0].split()
# for i in lst:
#     if i.startswith('$'):
#         print(i)


import requests,re

r = requests.get('https://www.trustpilot.com/review/www.amazon.com')

s = r.text
patt = r'https?://[^\s\'"<>\\,]+'
x = re.findall(patt ,s)
for i in x:
    print(i)
print(len(x))
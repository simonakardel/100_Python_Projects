import requests
import os

url = input('Enter the name of the website:')

request = requests.get(url)
text = request.text

img_list = []

text_list = text.split('img')

def locate_image(e):
    i = e.find('"')

    img_url = e.split('"')
    img_url = img_url[1]
    img_list.append(img_url)

for e in text_list:
    if 'src' in e:
        locate_image(e)

#print(img_list)

os.mkdir('src')
os.chdir('src')

for i in img_list:
    newUrl = url.rsplit('/', 1)
    req = requests.get(f'{newUrl[0]}{i}', stream=True)

    with open(i[4:], 'wb') as f:
        for chunk in req:
            f.write(chunk)

os.chdir('..')

with open('index.html', 'w') as f:
    f.write(text)
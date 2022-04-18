import requests
import os

url = input('Enter image url: ')
path = input('Enter path to where you wanna save the image file (blank for current folder) : ')
name = input('Enter name for your image file: ')
extension = url.split('.')[-1]

if len(extension) > 4:
    extension = 'jpeg'

if not os.path.exists(path):
    os.mkdir(path)

if os.path.exists(f'{path}/{name}.{extension}'):
    print('Image already exists in the path specified!!!')
    exit(1)

req = requests.get(url)

with open(f'{path}/{name}.{extension}', 'wb') as f:
    f.write(req.content)

print(f'Image saved to {path}/{name}.{extension}')

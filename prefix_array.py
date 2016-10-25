'''
Abdurrauf Muhammad

prefix_array.py
'''

import requests

r = requests.post('http://challenge.code2040.org/api/prefix'
, data ={'token' : '532856fe705c8a089d3e4b8213327687'})

dict = r.json()
prefix = dict.get('prefix')
array = dict.get('array')
new_array = []

#iterates through array and adds strings without prefix to new array
for i in array:
    if(i[:4] != prefix):
        new_array.append(i)
        
d = {'array': new_array, 'token':"532856fe705c8a089d3e4b8213327687"}
print(d)

r = requests.post('http://challenge.code2040.org/api/prefix/validate', json = d)

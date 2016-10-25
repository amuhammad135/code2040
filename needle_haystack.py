'''
Abdurrauf Muhammad

needle_haystack.py
'''

import requests

r = requests.post('http://challenge.code2040.org/api/haystack'
, data ={'token' : '532856fe705c8a089d3e4b8213327687'})

#dictionary given
dict = r.json()

#string needed to find in array
needle = dict.get('needle')

#array to be iterated through
haystack = dict.get('haystack')

#iterates through array for position of needle
for i in range(0,len(haystack)):
    if(haystack[i] == needle):
        needle = i
        break

r = requests.post('http://challenge.code2040.org/api/haystack/validate'
, params ={'token' : '532856fe705c8a089d3e4b8213327687' , 'needle' : needle})


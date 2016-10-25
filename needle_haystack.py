import requests

r = requests.post('http://challenge.code2040.org/api/haystack'
, data ={'token' : '532856fe705c8a089d3e4b8213327687'})

dict = r.json()

needle = dict.get('needle')
haystack = dict.get('haystack')

for i in range(0,len(haystack)):
    if(haystack[i] == needle):
        needle = i
        break

r = requests.post('http://challenge.code2040.org/api/haystack/validate'
, params ={'token' : '532856fe705c8a089d3e4b8213327687' , 'needle' : needle})
r.text

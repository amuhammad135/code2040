import requests

r = requests.post('http://challenge.code2040.org/api/reverse'
, data ={'token' : '532856fe705c8a089d3e4b8213327687'})

#reverses string
rev = r.text[::-1]

r = requests.post('http://challenge.code2040.org/api/reverse/validate'
, params ={'token' : '532856fe705c8a089d3e4b8213327687' , 'string' : rev})



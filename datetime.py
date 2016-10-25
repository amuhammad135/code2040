import requests
import datetime
import dateutil.parser

r = requests.post('http://challenge.code2040.org/api/dating'
, data ={'token' : '532856fe705c8a089d3e4b8213327687'})

dict = r.json()


interval = dict.get('interval')
ds = dict.get('datestamp')

a = dateutil.parser.parse(ds)
b = a + datetime.timedelta(0,interval)

new = (str(b.date())+"T"+str(b.time())+"Z")

d = {'datestamp': new, 'token':"532856fe705c8a089d3e4b8213327687"}
print(d)


r = requests.post('http://challenge.code2040.org/api/dating/validate', json=d)

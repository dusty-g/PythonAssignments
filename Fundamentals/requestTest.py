import requests

url = 'http://www.msn.com/'
r = requests.get('https://api.github.com/events')
print r.raw.read(14)
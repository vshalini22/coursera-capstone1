import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'


address = input('Enter location: ')

url = serviceurl + urllib.parse.urlencode(
        {'address': address})

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
        js = json.loads(data)
except:
        js = None

    
place_id = js['results'][0]['place_id']
print('Place id',place_id)
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    #url = urllib.parse.urlencode({'address': address})
    #print('Retrieving', url)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('count')
    print (results)
    lat = results.text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #/location = results[0].find('formatted_address').text

    print('lat', lat)
    #/print(location)

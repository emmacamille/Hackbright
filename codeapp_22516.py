from urllib2 import urlopen 
from json import load

apiUrl = "https://data.sfgov.org/resource/wwmu-gmzc.json"

response = urlopen(apiUrl)
json_obj = load(response)

print json_obj


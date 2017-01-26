import csv
import requests

print('What is the weather like on Fourth of July?')
#csv = open("csvproject.csv", "w")
endpoint = 'https://api.darksky.net/forecast/'
apikey = '032150d8fc8bab83f50c8281740b485b'
lat = str(input('what is your latitude? '))
lon = str(input('what is your longitude? '))
year = str(input('what year do you want to search for? '))
time = [year]-[07]-[04]T[12]:[01]:[01][GMT]

#make url for request
url = endpoint + '/' apikey + '/' + lat + ',' + lon + ',' + time
print(url)

#make a request and save it to a variable
r = requests.get(url)
print(r.url)
results - r.json()
print(results)
#csvwriter.writerow(results)

#process information


#print the weather for that specific fourth of july


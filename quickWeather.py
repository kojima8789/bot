#! python3
#quickWeather.py

import json,requests,sys

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# TODO

APPID = 'a9a2238e4624c8c1203e49d4e0e3643f'

url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&cnt=3&appid={}'.format(location,APPID)

response = requests.get(url)
response.raise_for_status()

# TODO

weather_data = json.loads(response.text)


w = weather_data['list']

print('{}の現在の天気:'.format(location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print('明日:')
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])
print()
print('明後日:')
print(w[2]['weather'][0]['main'],'-',w[2]['weather'][0]['description'])



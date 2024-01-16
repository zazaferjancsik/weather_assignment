import json
from csv import DictReader

with open('precipitation.json', encoding='utf-8') as file:               #opening json file
    precipitation = json.load(file)

with open('stations.csv') as file:           #opening csv file
    reader = DictReader(file)
    stations = list(reader)

results = {}

for station in stations:                                #creating library for each station without calculated data
    results[station['Location']] = {}
    results[station['Location']]['station'] = station['Station']
    results[station['Location']]['state'] = station['State']
    results[station['Location']]['total_monthly_precipitation'] = {}
    results[station['Location']]['total_yearly_precipitation'] = 0
    results[station['Location']]['relative_monthly_precipitation'] = 0
    results[station['Location']]['relative_yearly_precipitation'] = 0

for data in precipitation:
    if data['station'] == 'GHCND:USW00093814':
        data['location'] = 'Cincinnati'
    elif data['station'] == 'GHCND:US1WAKG0038':
        data['location'] = 'Seattle'
    elif data['station'] == 'GHCND:USC00513317':
        data['location'] = 'Maui'
    elif data['station'] == 'GHCND:US1CASD0032':
        data['location'] = 'San Diego'
    

# for data in precipitation:
#     if int(data['date'].split('-')[1]) in results[data[]]

with open('results.json', 'w', encoding='utf-8') as file:               #writing json file
    json.dump(results, file, indent=4)
with open('precipitation_edited.json', 'w', encoding='utf-8') as file:               #writing json file
    json.dump(precipitation, file, indent=4)

datee = '2020-01-01'

print(int(datee.split('-')[1]))




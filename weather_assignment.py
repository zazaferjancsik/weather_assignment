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
    results[station['Location']]['relative_monthly_precipitation'] = {}
    results[station['Location']]['relative_yearly_precipitation'] = 0

for data in precipitation:                          #adding name of the location, so it is easier to sort out each data
    if data['station'] == 'GHCND:USW00093814':
        data['location'] = 'Cincinnati'
    elif data['station'] == 'GHCND:US1WAKG0038':
        data['location'] = 'Seattle'
    elif data['station'] == 'GHCND:USC00513317':
        data['location'] = 'Maui'
    elif data['station'] == 'GHCND:US1CASD0032':
        data['location'] = 'San Diego'
    

for data in precipitation:                              #adding up all monthly precipitation
    if int(data['date'].split('-')[1]) not in results[data['location']]['total_monthly_precipitation']:
        results[data['location']]['total_monthly_precipitation'][int(data['date'].split('-')[1])] = data['value']
    else:
        results[data['location']]['total_monthly_precipitation'][int(data['date'].split('-')[1])] += data['value']

for station in results:                         #adding up the monthly precipitation to get the yearly, for each station
    for i in range(1, 13):
        results[station]['total_yearly_precipitation'] += results[station]['total_monthly_precipitation'][i]

for station in results:                     #calculating relative monthly precipitation
    for i in range(1, 13):
        results[station]['relative_monthly_precipitation'][i] = results[station]['total_monthly_precipitation'][i] / results[station]['total_yearly_precipitation']

with open('results.json', 'w', encoding='utf-8') as file:               #writing json file
    json.dump(results, file, indent=4)
with open('precipitation_edited.json', 'w', encoding='utf-8') as file:               #writing json file
    json.dump(precipitation, file, indent=4)





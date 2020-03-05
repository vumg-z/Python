#! /usr/bin/python3
import http.client, json, random, time

# init time
initialTime = time.time()

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'cf37aebe74444dc2a8c8e463b8ebbff7' }
connection.request('GET', '/v2/teams/86', None, headers )
response = json.loads(connection.getresponse().read().decode())

names = []

for i in response['squad']:
    names.append(i['name'])

print(names[random.randint(0,len(names))])

finalTime = round(time.time() - initialTime, 2)

print(str(finalTime)+" seconds")

#! /usr/bin/python3
import http.client, json, random, time

try:
    # init time
    initialTime = time.time()
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': 'cf37aebe74444dc2a8c8e463b8ebbff7' }
    connection.request('GET', '/v2/teams/86', None, headers )
    response = json.loads(connection.getresponse().read().decode())

    names = []

    for i in response['squad']:
        names.append(i['name'])

    finalTime = round(time.time() - initialTime, 2)
    print(names[random.randint(0,len(names))], "in", str(finalTime), "seconds")

except Exception as e:
    print("real madrid player not available: request error")


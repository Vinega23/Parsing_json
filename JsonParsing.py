import json
from datetime import timezone
import datetime

with open('sample-data.json') as file:
    data = json.load(file)

index = 0

for item in data:
    print(f"\nContainer {index}:")
    print(f"Name: {item['name']}")
    if item['state'] and ['cpu'] is not None:
        print(f"Cpu usage: {item['state']['cpu']['usage']}")
    else:
        print("Cpu usage: 0")
    if item['state'] and ['memory'] is not None:
        print(f"Memory usage: {item['state']['memory']['usage']}")
    else:
        print("Memory usage: 0")

    print(f"Created at: {item['created_at']}")
    print(f"Status: {item['status']}")
    if item['state'] and ['network'] is not None:
        print("IP addresses:")
        if 'docker0' in item['state']['network']:
            print(f"docker0: {item['state']['network']['docker0']['addresses'][0]['address']}")
        else:
            print("docker0: None")
        if 'eth0' in item['state']['network']:
            print(f"eth0: {item['state']['network']['eth0']['addresses'][0]['address']}")
        else:
            print("eth0: None")
        if 'lo' in item['state']['network']:
            print(f"lo: {item['state']['network']['lo']['addresses'][0]['address']}")
        else:
            print("lo: None")

    else:
        print("IP addresses: None")
    index += 1

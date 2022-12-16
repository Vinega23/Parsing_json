import json
with open('sample-data.json', 'r') as file:
    data = json.load(file)

ret = '['
index = 0

for item in data:
    ret += '{'
    ret += f'"_id" : "Container{index}", '
    ret += f'"name" : "{item["name"]}", '
    if item['state'] and ['cpu'] is not None:
        ret += f'"cpu_usage" : "{item["state"]["cpu"]["usage"]}", '
    else:
        ret += '"cpu_usage" : 0, "'
    if item['state'] and ['memory'] is not None:
        ret += f'"memory_usage" : "{item["state"]["memory"]["usage"]}", '
    else:
        ret += '"memory_usage" : 0, '
    ret += f'"created_at" : "{item["created_at"]}", '
    ret += f'"Status" : "{item["status"]}", '
    if item['state'] and ['network'] is not None:
        ret += '"IP addresses" : {'
        if 'docker0' in item['state']['network']:
            ret += f'"docker0" : "{item["state"]["network"]["docker0"]["addresses"][0]["address"]}", '
        else:
            ret += '"docker0" : "none", '
        if 'eth0' in item['state']['network']:
            ret += f'"eth0" : "{item["state"]["network"]["eth0"]["addresses"][0]["address"]}", '
        else:
            ret += '"eth0" : "none"'
        if 'lo' in item['state']['network']:
            ret += f'"lo" : "{item["state"]["network"]["lo"]["addresses"][0]["address"]}"'
        else:
            ret += '"lo" : "none",'
        ret += '}'
    else:
        ret += '"IP addresses" : "none"'
    ret += '},'
    index += 1
ret += ']'

print(ret)

pretty = [{"_id" : "Container0", "name" : "Mobile-applications-UI-test", "cpu_usage" : 0, "memory_usage" : 52985856, "created_at" : "2020-05-19T16:23:07+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "172.17.0.1", "eth0" : "10.17.170.111", "lo" : "127.0.0.1"}},{"_id" : "Container1", "name" : "docker-at", "cpu_usage" : 0, "memory_usage" : 0, "created_at" : "2020-03-01T01:03:08+01:00", "Status" : "Stopped", "IP addresses" : "none"},{"_id" : "Container2", "name" : "docker-logman-prod-env", "cpu_usage" : 0, "memory_usage" : 763113472, "created_at" : "2020-06-12T16:12:45+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "172.17.0.1", "eth0" : "10.17.168.70", "lo" : "127.0.0.1"}},{"_id" : "Container3", "name" : "ecr-messenger-test", "cpu_usage" : 0, "memory_usage" : 2099625984, "created_at" : "2020-03-13T13:17:46+01:00", "Status" : "Running", "IP addresses" : {"docker0" : "172.17.0.1", "eth0" : "10.17.168.114", "lo" : "127.0.0.1"}},{"_id" : "Container4", "name" : "fastkafka-at-2006", "cpu_usage" : 0, "memory_usage" : 76591104, "created_at" : "2020-06-06T19:58:39+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "none", "eth0" : "10.17.164.107", "lo" : "127.0.0.1"}},{"_id" : "Container5", "name" : "ftp-test", "cpu_usage" : 0, "memory_usage" : 57446400, "created_at" : "2019-10-10T12:42:51+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "none", "eth0" : "10.17.170.231", "lo" : "127.0.0.1"}},{"_id" : "Container6", "name" : "genie-docker-test", "cpu_usage" : 0, "memory_usage" : 632188928, "created_at" : "2020-05-14T14:50:00+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "172.17.0.1", "eth0" : "10.17.161.11", "lo" : "127.0.0.1"}},{"_id" : "Container7", "name" : "gitlab-ci-runner-test", "cpu_usage" : 0, "memory_usage" : 86732800, "created_at" : "2020-06-08T12:40:16+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "172.17.0.1", "eth0" : "10.17.161.22", "lo" : "127.0.0.1"}},{"_id" : "Container8", "name" : "kafka-ui", "cpu_usage" : 0, "memory_usage" : 190758912, "created_at" : "2020-06-24T17:03:25+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "172.17.0.1", "eth0" : "10.17.164.96", "lo" : "127.0.0.1"}},{"_id" : "Container9", "name" : "lmio-deploy-single-test", "cpu_usage" : 0, "memory_usage" : 55820288, "created_at" : "2020-05-25T12:45:43+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "172.17.0.1", "eth0" : "10.17.166.22", "lo" : "127.0.0.1"}},{"_id" : "Container10", "name" : "scep-testing", "cpu_usage" : 0, "memory_usage" : 123838464, "created_at" : "2020-06-09T14:51:42+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "none", "eth0" : "10.17.167.80", "lo" : "127.0.0.1"}},{"_id" : "Container11", "name" : "seacat-pki-test", "cpu_usage" : 0, "memory_usage" : 411295744, "created_at" : "2020-04-16T12:07:06+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "172.17.0.1", "eth0" : "10.17.169.13", "lo" : "127.0.0.1"}},{"_id" : "Container12", "name" : "teskalabs-apm", "cpu_usage" : 0, "memory_usage" : 667648, "created_at" : "2019-08-23T17:16:28+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "none", "eth0" : "10.17.162.236", "lo" : "127.0.0.1"}},{"_id" : "Container13", "name" : "tlbackup-server", "cpu_usage" : 0, "memory_usage" : 27820032, "created_at" : "2019-08-19T12:08:31+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "none", "eth0" : "10.17.165.109", "lo" : "127.0.0.1"}},{"_id" : "Container14", "name" : "wiki-test", "cpu_usage" : 0, "memory_usage" : 1527808, "created_at" : "2019-10-22T13:51:14+02:00", "Status" : "Running", "IP addresses" : {"docker0" : "none", "eth0" : "10.17.165.138", "lo" : "127.0.0.1"}},{"_id" : "Container15", "name" : "zookeeper-ui", "cpu_usage" : 0, "memory_usage" : 698519552, "created_at" : "2020-03-11T13:38:13+01:00", "Status" : "Running", "IP addresses" : {"docker0" : "172.17.0.1", "eth0" : "10.17.164.94", "lo" : "127.0.0.1"}},{"_id" : "Container16", "name" : "zzz-mautic-test", "cpu_usage" : 0, "memory_usage" : 45236224, "created_at" : "2019-11-21T13:16:43+01:00", "Status" : "Running", "IP addresses" : {"docker0" : "none", "eth0" : "fd87:1cf1:9a65:0:216:3eff:feec:8db", "lo" : "127.0.0.1"}}]
print(json.dumps(pretty, indent= 4))









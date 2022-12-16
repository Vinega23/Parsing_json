import asyncio
import json
import aiofiles

async def get_json():
    async with aiofiles.open('sample-data.json', mode="rb") as f:
        db = json.loads(await f.read())
        return db
async def main():
    task1 = asyncio.create_task(get_json())
    data = await task1
    task2 = asyncio.create_task(get_data(data))
    print(await task2)
async def get_data(data):
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
    return ret
if __name__ == '__main__':
    asyncio.run(main())



import requests
import json

url = 'https://akabab.github.io/superhero-api/api'
hero_list = ['Hulk','Captain America','Thanos']
num = 1
i = 0
resp = requests.get(url + f'/all.json')

for hero in hero_list:
    for i in resp.json():
        if hero in i['name']:
            hero_int = {}
            hero_int.update({ i['name'] : i['powerstats']['intelligence']})

def hero_vers():
    if hero_int['Hulk'] > hero_int['Captain America'] and hero_int['Hulk'] > hero_int['Thanos']:
        print('Самый высокий уровень интелекта у Халка')
    elif hero_int['Captain America'] > hero_int['Hulk'] and hero_int['Captain America'] > hero_int['Thanos']:
        print('Самый высокий уровень интелекта у Капитана Америки')
    elif hero_int['Thanos'] > hero_int['Captain America'] and hero_int['Thanos'] > hero_int['Hulk']:
        print('Самый высокий уровень интелекта у Таноса')
    else:
        print('Ошибка')

print(hero_vers())

host = 'https://cloud-api.yandex.net:443'

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    def upload(self):
        uri = 'v1/disk/resources/'
        file = {'photo':open('test.png')}
        requests.post(uri, files = file)

if __name__ == '__main__':
    path_to_file = 'v1/disk/resources/Kulturniy_zaba.png'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
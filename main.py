import requests
import json

url = 'https://akabab.github.io/superhero-api/api'
hero_list = ['Hulk','Captain America','Thanos']
num = 1
i = 0
resp = requests.get(url + f'/id/{num}.json')

while i < len(resp.json()):
    i += 1
    num += 1
    int_list = {}
    for hero in hero_list:
        if resp.json()['name'] == hero:
            int_list.update({resp.json()['name'] : resp.json()['powerstats']['intelligence']})

host = 'https://cloud-api.yandex.net:443'

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        self.file_path = file_path
        file_path = 'E:\Photoshop Galery\Kulturniy_zaba.png'
        uri = 'v1/disk/resources/'
        requests_url = self.file_path + uri
        response = requests.put(requests_url)


if __name__ == '__main__':
    path_to_file = 'v1/disk/resources/Kulturniy_zaba.png'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
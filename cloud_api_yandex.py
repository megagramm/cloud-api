"""
Модуль подключения и работы cloud-api.yandex.ru

2022 Andrey Grey megagramm@gmail.com
"""
import requests
import urllib.parse as UP


class CloudAPI:
    with open('token.txt') as tk:
        token = tk.readline()


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.base_host = "https://cloud-api.yandex.net:443/"

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload/'
        request_url = self.base_host + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()['href']

    def upload_to_disk(self, local_path, yandex_path):
        upload_url = self._get_upload_link(yandex_path)
        response = requests.put(upload_url, data=open(local_path, 'rb'), headers=self.get_headers())
        if response.status_code == 201:
            print(f"Успешно выгружен {local_path}")

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        path = file_path.split("/")
        file = path.pop()
        print(file)
        # return

        self.upload_to_disk(file_path,file)


if __name__ == '__main__':

    with open('token.txt') as tk:
        token = tk.readline()
    ya = YaUploader(token)
    for path_to_file in files:
        result = ya.upload(path_to_file)

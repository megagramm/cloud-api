from cloud_api_yandex import YaUploader
import os


def get_files_from_dir(path: str, absolute_path=False):
    """Считывает директорию с файлами"""
    full_path = f"{os.getcwd()}/{path}"
    files = sorted(os.listdir(full_path))
    result_files = []
    for file in files:
        if absolute_path:
            result_files.append(f"{full_path}/{file}")
        else:
            result_files.append(f"{path}/{file}")
    return result_files


with open('token.txt') as tk:
    token = tk.readline()

files = get_files_from_dir('sample_files')
print(files)
uploader = YaUploader(token)
for path_to_file in files:
    result = uploader.upload(path_to_file)


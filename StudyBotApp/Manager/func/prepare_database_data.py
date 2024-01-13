import os
import json
import Manager


json_path: str = 'static/jsons/data.json'

urls: list[str] = [
    "https://rsreu.ru/studentu/raspisanie-ekzamenov",
    "https://rsreu.ru/studentu/raspisanie-zanyatij",
]

paths: list[str] = ['exams', 'lessons']


def _(download_files) -> None:

    json_dict: dict = {}
    for path in paths:
        url: str = urls[paths.index(path)]
        full_path: str = 'static/' + path + '/'
        
        if download_files:
            folders: list[str] = Manager.download_files(url, full_path)
        else:
            folders: list[str] = [
                full_path + folder for folder in os.listdir(full_path)]
        
        list_all: list = []
        for folder in folders:
            list_all.extend(Manager.parse_file(folder, path + '/'))
        
        json_dict[path] = list_all
    with open(json_path, 'w') as f:
        json.dump(json_dict, f, indent=4, ensure_ascii=False)

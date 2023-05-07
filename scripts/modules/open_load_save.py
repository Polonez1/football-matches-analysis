import json


def open_json(relative_path: str, file_name: str):
    jsobject = open(relative_path + "\\" + file_name, "r")
    json_file = json.load(jsobject)
    return json_file

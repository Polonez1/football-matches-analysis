import json
import config


def open_json(relative_path: str, file_name: str):
    jsobject = open(config.CURRENT_PATH + relative_path + "\\" + file_name, "r")
    json_file = json.load(jsobject)
    return json_file

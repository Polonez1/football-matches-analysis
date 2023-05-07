import requests
import logging
import sys
import json

sys.path.append(".\\config\\")
import secret
import config


config.log


def connect_to_footystats(url: str, **kwargs):
    url = url.format(api_token=secret.API_TOKEN, season_id=secret.SEASON_ID, **kwargs)
    response = requests.get(url)
    logging.info(response.status_code)
    logging.info(response.request)
    return response


def get_json_API(response: requests):
    jsonObj = response.json()
    return jsonObj


if __name__ == "__main__":
    response = connect_to_footystats(url=config.TEAMS_URL)
    js = get_json_API(response)

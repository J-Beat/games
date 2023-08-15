import configparser as cnf
import json

def get_token() -> str:
    configPath = '/home/ivan/Projects/git/games/PRO_rf_bot/config/config.ini'
    config = cnf.ConfigParser()  # создаём объекта парсера
    config.read(configPath)
    token = config['TOKEN']['MAIN_TOKEN']
    return token


def get_texts() -> dict:
    with open("texts.json", "r") as read_file:
        data = json.load(read_file)
    return data


def get_all_buttons(path: dict) -> list:
    buttons_list = []
    for v in path.values():
        if type(v) == dict:
            val = get_all_buttons(v)
            buttons_list.extend(val)
        elif type(v) == str:
            buttons_list.append(v)
    return buttons_list
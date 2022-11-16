import configparser as cnf
import json

def get_token() -> str:
    configPath = 'config/config.ini'
    config = cnf.ConfigParser()  # создаём объекта парсера
    config.read(configPath)
    token = config['TOKEN']['TOKEN']
    ID = config['TOKEN']['ID']
    return token, ID

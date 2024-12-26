import configparser
import os
from webbrowser import Error

import pymysql

def getConfig():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'dbProperties.ini')
    config.read(config_path)
    return config

def getConnection():
    connect_config = {
        'host': getConfig()['SQL']['host'],
        'database': getConfig()['SQL']['database1'],
        'user': getConfig()['SQL']['user'],
        'password': getConfig()['SQL']['password']
    }
    conn = pymysql.connect(**connect_config)  #connect method accepts dictonary
    return conn

def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row

#print(getConfig()['SQL']['host'])
#print(getConnection())
#print(getConfig())
#url = 127.0.0.1:3306




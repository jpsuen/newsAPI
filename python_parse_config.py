import os


def read_db_config(database='server'):
    hostname = os.environ['newsAPIHost']
    dbuser = 'newsapi'
    dbname = 'newsAPI'
    dbpw = os.environ['newsAPIpw']
    if database != 'server':
        dbuser = 'redcap'
        hostname = 'localhost'
    db = {'host': hostname, 'user': dbuser, "db": dbname, 'passwd': dbpw}
    return db


def read_url_config(section='article'):
    url = 'https://newsapi.org/v1/articles'
    if section != 'article':
        url = 'https://newsapi.org/v1/sources'
    return url


def read_news_config(section='None'):
    apiToken = os.environ['newsAPIToken']
    api = {'apiKey': apiToken}
    if section == 'source':
        api['category'] = ''
        api['source'] = ''
    elif section == 'article':
        api['source'] = ''
    return api

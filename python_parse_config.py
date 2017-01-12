# Credit to: http://www.mysqltutorial.org/python-connecting-mysql-databases/ for inspiration

from configparser import ConfigParser


def read_db_config(filename='config.ini', section='mysql'):
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return db


def read_url_config(filename='config.ini', section='article'):
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to article
    if parser.has_section(section):
        url = parser.items(section)[0][1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return url


def read_news_config(filename='config.ini', section='None'):
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section
    api = {}
    payload = None

    # Always need to grab the token, if it exists
    if parser.has_section('apiToken'):
        token = parser.items('apiToken')
        for t in token:
            api[t[0]] = t[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    # If searching for article, return those variables
    if section == 'article':
        if parser.has_section('articleParams'):
            payload = parser.items('articleParams')
        else:
            raise Exception('{0} not found in the {1} file'.format(section, filename))

    # If searching for sources, return those variables
    if section == 'source':
        if parser.has_section('sourceParams'):
            payload = parser.items('sourceParams')
        else:
            raise Exception('{0} not found in the {1} file'.format(section, filename))

    if payload is not None:
        for l in payload:
            api[l[0]] = l[1]

    return api

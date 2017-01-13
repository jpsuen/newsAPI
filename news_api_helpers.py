from datetime import datetime


def id_fetch(cur):
    x = cur.fetchall()
    x = x[0][0]
    return x


def sanitize(x):
    x = x.replace("'", r"\'").encode('latin-1', 'ignore')
    return x


def date_clean(x='None'):
    str = '%Y-%m-%d %H:%M:%S'
    default = '2001-01-01 01:01:01'
    if x is 'None' or x is 'NULL' or x is None or (int(x[:4]) < 2000):
        x = datetime.strptime(default, str)
    else:
        if len(x) > 18:
            date = x[:10] + " " + x[11:19]
            try:
                x = datetime.strptime(date, str)
            except ValueError:
                x = datetime.strptime(default, str)
        else:
            x = datetime.strptime(default, str)
    return x




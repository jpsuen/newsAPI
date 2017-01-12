def id_fetch(cur):
    x = cur.fetchall()
    x = x[0][0]
    return x


def sanitize(x):
    x.replace("'", r"\'").encode('ascii', 'ignore')
    return x
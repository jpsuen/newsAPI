def id_fetch(cur):
    x = cur.fetchall()
    x = x[0][0]
    return x


def sanitize(x):
    x = x.replace("'", r"\'").encode('latin-1', 'ignore')
    return x

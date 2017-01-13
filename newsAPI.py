# encoding: latin-1
from python_parse_config import read_db_config, read_news_config, read_url_config
from news_api_helpers import id_fetch, sanitize
import requests
import MySQLdb


# Static Vars
sourceUrl = read_url_config(section='source')
articlesUrl = read_url_config(section='article')
sourcePayload = read_news_config(section='source')
articlePayload = read_news_config(section='article')

# Check List of Sources
data = requests.get(sourceUrl, params=sourcePayload).json()
srcLen = len(data['sources'])
srcList = data['sources']

# Open DB Connection
dbParams = read_db_config()
db = MySQLdb.connect(**dbParams)
cur = db.cursor()

# Get some basic data
cur.execute("SELECT * FROM sources")
dbSrc = cur.fetchall()

# Check DB for current sources & add, if needed
if srcLen > len(dbSrc):
    for src in range(0, srcLen):
        if srcList[src]['id'] not in dbSrc:
            sourceVars = {'source': data['sources'][src]['id'],
                          "description": sanitize(data['sources'][src]['description'])}
            sqlInsert = """INSERT INTO sources (source_name, source_description) VALUES
            ('%(source)s', '%(description)s');""" % sourceVars
            cur.execute(sqlInsert)
    db.commit()

for src in range(0, srcLen):
    articlePayload['source'] = dbSrc[src][1]
    data2 = requests.get(articlesUrl, params=articlePayload).json()
    for art in range(0, len(data2['articles'])):
        sqlq = "SELECT COUNT(1) FROM articles WHERE url = '%(url)s';" % {'url': data2['articles'][art]['url']}
        cur.execute(sqlq)
        if cur.fetchone()[0]:
            break
        else:
            author = data2['articles'][art]['author']
            if author is None:
                authID = 1
            elif author is not None:
                author = sanitize(author)
                sqlq = "SELECT COUNT(1) FROM author_list WHERE author_name = '%(name)s';" % {'name': author}
                cur.execute(sqlq)
                if cur.fetchone()[0]:
                    cur.execute("SELECT * FROM author_list WHERE author_name = '%(auth)s' LIMIT 1;" % {'auth': author})
                    authID = id_fetch(cur)
                else:
                    sqlInsert = "INSERT INTO author_list (author_name) VALUES ('%(auth)s');" % {'auth': author}
                    cur.execute(sqlInsert)
                    db.commit()
                    print(author)
                    cur.execute("SELECT LAST_INSERT_ID()")
                    authID = id_fetch(cur)

            # Assign variables
            source_id = dbSrc[src][0]
            publishedAt = data2['articles'][art]['publishedAt']
            title = data2['articles'][art]['title']
            description = data2['articles'][art]['description']
            url = data2['articles'][art]['url']
            urlToImage = data2['articles'][art]['urlToImage']
            articleVars = {'src': source_id, 'pub': publishedAt, 'title': title,
                           'desc': description, 'url': url, 'urlImg': urlToImage}
            for v in articleVars.keys():
                if articleVars[v] is None:
                    articleVars[v] = 'NULL'
                if type(articleVars[v]) != long:
                    articleVars[v] = sanitize(articleVars[v])
            # Put each article into article table of DB

            sqlInsert = """INSERT INTO articles (source_id, publishedAt, title, description, url, urlToImage) VALUES
                        ('%(src)s', '%(pub)s', '%(title)s', '%(desc)s', '%(url)s', '%(urlImg)s');""" % articleVars
            cur.execute(sqlInsert)
            db.commit()

            # Get article_id from new article
            cur.execute("SELECT LAST_INSERT_ID()")
            artID = id_fetch(cur)

            # Connect authors with articles in author table
            artListVars = {'artId': artID, 'autId': authID}
            sqlInsert = """INSERT INTO author (article_id, author_id) VALUES
                        ('%(artId)s', '%(autId)s');""" % artListVars
            cur.execute(sqlInsert)
            db.commit()

db.close()


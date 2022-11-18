import psycopg2 as psyco
import urllib.parse as up

def connect_db():
    """Establish connection to db"""
    conn = None
    try:
        up.uses_netloc.append("postgres")
        url = up.urlparse('postgres://syjanunk:JeGdVqc95UOUcnYmW94ZZ5jdvEQXYn0K@peanut.db.elephantsql.com/syjanunk')
        conn = psyco.connect(database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
    except (Exception, psyco.DatabaseError) as e:
        print(e)
    finally:
        return conn

def close_db(cursor, con):
    """Close all connections to db"""
    cursor.close()
    con.close()

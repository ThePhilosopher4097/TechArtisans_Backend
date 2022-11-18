import db
import psycopg2 as psyco

CREATE_USER = """
              CREATE TABLE IF NOT EXISTS student (
                  name     VARCHAR(50),
                  email    VARCHAR(60) PRIMARY KEY,
                  phone    VARCHAR(15),
                  password VARCHAR(40),
                  country  VARCHAR(40)
              )
              """

conn = None
try:
    conn = db.connect_db()
    cur  = conn.cursor()

    queries = (
        CREATE_USER,    
    )

    for query in queries:
        cur.execute(query)

    cur.close()
    conn.commit()

except (Exception, psyco.DatabaseError) as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
        print('Database closed')

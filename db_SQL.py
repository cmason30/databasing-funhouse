import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='database3' user='postgres' password='stefflab' host= 'localhost' port='5432'")

    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database3' user='postgres' password='stefflab' host= 'localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


# insert("Coffee Cup", 5, 10.5)


def view():
    conn = psycopg2.connect("dbname='database3' user='postgres' password='stefflab' host= 'localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='database3' user='postgres' password='stefflab' host= 'localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database3' user='postgres' password='stefflab' host= 'localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    conn.commit()
    conn.close()


create_table()
update(20, 15.0, "Orange")
print(view())
# insert("Orange", 10, 15)
# update(11, 6, "Coffee")
# print(view())
# 1 connect to database
# 2 create a cursor object
# 3 Write an SQL query
# 4 Commit changes
# 5 Close database connection
from brnspreadsheetreader import read_brn_jyorg
import psycopg2

# just connect values to their respective variables in these functions
def insert_experiment(original_file, new_file, r2, K, Tau, Half_Life):
    conn = psycopg2.connect("dbname='defaultdb' user='doadmin' password='mipnx2kio6ad5bcb' host= 'db-postgresql-sfo2-46299-do-user-6974358-0.db.ondigitalocean.com' port='25060' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO experiment VALUES (%s, %s, %s, %s, %s, %s)", (original_file, new_file, r2, K, Tau, Half_Life))
    conn.commit()
    conn.close()


def insert_intervals(time, current_Na):
    conn = psycopg2.connect("dbname='defaultdb' user='doadmin' password='mipnx2kio6ad5bcb' host= 'db-postgresql-sfo2-46299-do-user-6974358-0.db.ondigitalocean.com' port='25060' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO intervals VALUES (%s, %s)",
                (time, current_Na))
    conn.commit()
    conn.close()


#category variable can be the drug name
#filename would be labeling name of the overarching file of experiments
def insert_mouse(category, filename):
    conn = psycopg2.connect("dbname='defaultdb' user='doadmin' password='mipnx2kio6ad5bcb' host= 'db-postgresql-sfo2-46299-do-user-6974358-0.db.ondigitalocean.com' port='25060' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO mouses VALUES (%s, %s)", (category, filename))
    conn.commit()
    conn.close()

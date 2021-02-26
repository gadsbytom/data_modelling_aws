import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        print('starting loading!')
        cur.execute(query)
        conn.commit()
        print('loaded!!')


def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    print('we started the connection!!')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    print('we established the connection!!')
    load_staging_tables(cur, conn)
    print('we copied the data from S3 to Redshift!!')
    #insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
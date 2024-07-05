import psycopg2
from psycopg2 import pool


class DataBaseConnectionManager:

    def __init__(self):
        self.thread_pool = pool.ThreadedConnectionPool(2, 10,
                                                       user="postgres",
                                                       password="postgres",
                                                       host="127.0.0.1",
                                                       port="5436",
                                                       database="postgres")

    def close_connection_cursor(self, cursor):
        cursor.close()

    def get_connection_cursor(self) -> psycopg2.Cu:
        conn = self.thread_pool.getconn(self)
        return conn.cursor()

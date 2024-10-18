from psycopg2 import pool
import os


class DatabaseConfigurationProp:
    def __init__(self):
        self.user = os.getenv("PHONE_BOOK_DATABASE_USER_NAME")
        self.password = os.getenv("PHONE_BOOK_DATABASE_PASSWORD")
        self.host = os.getenv("PHONE_BOOK_DATABASE_HOST")
        self.port = os.getenv("PHONE_BOOK_DATABASE_PORT")
        self.database = os.getenv("PHONE_BOOK_DATABASE_NAME")


class DataBaseConnectionManager:

    def __init__(self, configuration: DatabaseConfigurationProp):
        print(self.user)
        print(self.password)
        print(self.host)
        print(self.port)
        print(self.database)
        self.thread_pool = pool.ThreadedConnectionPool(2, 5,
                                                       user=configuration.user,
                                                       password=configuration.password,
                                                       host=configuration.host,
                                                       port=configuration.port,
                                                       database=configuration.database)

    def close_connection_cursor(self, cursor):
        self.thread_pool.getconn(self).commit()
        cursor.close()

    def get_connection_cursor(self):
        conn = self.thread_pool.getconn(self)
        return conn.cursor()

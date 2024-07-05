from domain.PhoneBook import PhoneBookRepository, PhoneBook
from infrastructure.database.DataBaseConnectionManager import DataBaseConnectionManager


class PostgresqlPhoneBookRepository(PhoneBookRepository):

    def __init__(self):
        self.data_base_connection_manager = DataBaseConnectionManager()

    def get_records(self, user_name):
        cursor = self.data_base_connection_manager.get_connection_cursor()

        cursor.execute(f"SELECT * FROM PHONE_BOOK WHERE USER_NAME='{user_name}'")
        phone_book = self.row_mapper(cursor.fetchall())

        self.data_base_connection_manager.close_connection_cursor(cursor)
        return phone_book

    def save(self, phone_book_record: PhoneBook):
        cursor = self.data_base_connection_manager.get_connection_cursor()
        cursor.execute(
            f"""
                INSERT INTO PHONE_BOOK (user_name, contact_name,phone_number,birth_date )
                VALUES ('{phone_book_record.user_name}', '{phone_book_record.contact_name}', '{phone_book_record.phone_number}', '{phone_book_record.birth_date}') 
                ON CONFLICT(user_name, contact_name) DO UPDATE SET phone_number='{phone_book_record.phone_number}', birth_date='{phone_book_record.birth_date}'
            """)
        self.data_base_connection_manager.close_connection_cursor(cursor)

    def delete(self, user_name: str, contact_name: str):
        cursor = self.data_base_connection_manager.get_connection_cursor()
        cursor.execute(f"DELETE FROM PHONE_BOOK WHERE user_name='{user_name}' AND contact_name='{contact_name}'")
        self.data_base_connection_manager.close_connection_cursor(cursor)

    @staticmethod
    def row_mapper(rows):
        phone_book = []

        for row in rows:
            phone_book.append(
                PhoneBook(user_name=row[0], contact_name=row[1], phone_number=row[2], birth_date=row[3])
            )
        return phone_book

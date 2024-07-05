from domain.PhoneBook import PhoneBookRepository, PhoneBook
from infrastructure.database.DataBaseConnectionManager import DataBaseConnectionManager


class PostgresqlPhoneBookRepository(PhoneBookRepository):

    def __init__(self):
        self.data_base_connection_manager = DataBaseConnectionManager()

    def get_records(self, user_name):
        cursor = self.data_base_connection_manager.get_connection_cursor()
        cursor.execute(f"SELECT * FROM PHONE_BOOK WHERE USER_NAME={user_name}")
        self.data_base_connection_manager.close_connection_cursor(cursor)

    def save(self, phone_book_record: PhoneBook):
        cursor = self.data_base_connection_manager.get_connection_cursor()
        cursor.execute(
            f"INSERT INTO PHONE_BOOK (user_name, contact_name,phone_number,birth_date ) VALUES ('{phone_book_record.user_name}', '{phone_book_record.contact_name}', '{phone_book_record.phone_number}', '{phone_book_record.birth_date}')")
        self.data_base_connection_manager.close_connection_cursor(cursor)

    def delete(self, user_name: str, contact_name: str):
        cursor = self.data_base_connection_manager.get_connection_cursor()
        cursor.execute(f"DELETE FROM PHONE_BOOK WHERE user_name={user_name} AND contact_name={contact_name}")
        self.data_base_connection_manager.close_connection_cursor(cursor)

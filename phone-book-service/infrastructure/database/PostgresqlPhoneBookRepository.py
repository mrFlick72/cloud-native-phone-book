from domain import PhoneBook
from domain.PhoneBook import PhoneBookRepository


class PostgresqlPhoneBookRepository(PhoneBookRepository):

    def get_records(self, user_name):
        pass

    def save(self, phone_book_record: PhoneBook):
        pass

    def delete(self, phone_book_record: PhoneBook):
        pass

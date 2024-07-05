from domain.PhoneBook import PhoneBookRepository, PhoneBook
import datetime


class InMemoryPhoneBookRepository(PhoneBookRepository):

    def get_records(self, user_name) -> [PhoneBook]:
        result = list[PhoneBook(
            user_name='vvaudi',
            contact_name="Eva Therese",
            phone_number="333 23 23 233",
            birth_date=datetime.date.today()
        )]
        return result

    def save(self, phone_book_record: PhoneBook):
        pass

    def delete(self, phone_book_record: PhoneBook):
        pass

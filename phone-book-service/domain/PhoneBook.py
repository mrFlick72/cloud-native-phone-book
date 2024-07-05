import dataclasses
import datetime


@dataclasses.dataclass
class PhoneBook:
    user_name: str
    contact_name: str
    phone_number: str
    birth_date: datetime.date


class PhoneBookRepository:

    def get_records(self, user_name) -> list[PhoneBook]:
        pass

    def save(self, phone_book_record: PhoneBook):
        pass

    def delete(self, phone_book_record: PhoneBook):
        pass


class GetPhoneBookRecords:

    def __init__(self, repository: PhoneBookRepository):
        self.repository = repository

    def execute(self, user_name: str) -> list[PhoneBook]:
        print(self.repository)
        return self.repository.get_records(user_name)


class SavePhoneBookRecord:

    def __init__(self, repository: PhoneBookRepository):
        self.repository = repository

    def execute(self, phone_book_record: PhoneBook):
        self.repository.save(phone_book_record)


class DeletePhoneBookRecord:

    def __init__(self, repository: PhoneBookRepository):
        self.repository = repository

    def execute(self, phone_book_record: PhoneBook):
        self.repository.delete(phone_book_record)

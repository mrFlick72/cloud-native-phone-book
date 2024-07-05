import dataclasses
import datetime


@dataclasses.dataclass
class PhoneBook:
    user_name: str
    contact_name: str
    phone_number: str
    birth_date: datetime.date

    def __hash__(self):
        return hash(self.user_name) + hash(self.contact_name)

    def __eq__(self, other):
        return self.user_name == other.user_name and self.contact_name == other.contact_name


class PhoneBookRepository:

    def get_records(self, user_name):
        pass

    def save(self, phone_book_record: PhoneBook):
        pass

    def delete(self, user_name: str, contact_name: str):
        pass


class GetPhoneBookRecords:

    def __init__(self, repository: PhoneBookRepository):
        self.repository = repository

    def execute(self, user_name: str) -> list[PhoneBook]:
        return self.repository.get_records(user_name)


class SavePhoneBookRecord:

    def __init__(self, repository: PhoneBookRepository):
        self.repository = repository

    def execute(self, phone_book_record: PhoneBook):
        self.repository.save(phone_book_record)


class DeletePhoneBookRecord:

    def __init__(self, repository: PhoneBookRepository):
        self.repository = repository

    def execute(self, user_name: str, contact_name: str):
        self.repository.delete(user_name, contact_name)

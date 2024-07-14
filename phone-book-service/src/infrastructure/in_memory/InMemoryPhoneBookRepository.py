from domain.PhoneBook import PhoneBookRepository, PhoneBook


class InMemoryPhoneBookRepository(PhoneBookRepository):

    def __init__(self):
        self.storage = set([])

    def get_records(self, user_name) -> list[PhoneBook]:
        return self.storage

    def save(self, phone_book_record: PhoneBook):
        try:
            self.storage.remove(phone_book_record)
        except:
            pass

        self.storage.add(phone_book_record)

    def delete(self, user_name: str, contact_name: str):
        try:
            self.storage.remove(
                PhoneBook(user_name=user_name,
                          contact_name=contact_name,
                          phone_number=None,
                          birth_date=None
                          )
            )
        except:
            pass

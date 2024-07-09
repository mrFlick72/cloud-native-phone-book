from domain.PhoneBook import GetPhoneBookRecords, SavePhoneBookRecord, DeletePhoneBookRecord
from infrastructure.database.PostgresqlPhoneBookRepository import PostgresqlPhoneBookRepository
from web.PhoneBookEndPoint import PhoneBookEndPoint


@staticmethod
def application_init(app):
    repository = PostgresqlPhoneBookRepository()
    get_phone_book_records = GetPhoneBookRecords(repository)
    update_phone_book_record = SavePhoneBookRecord(repository)
    delete_phone_book_record = DeletePhoneBookRecord(repository)

    PhoneBookEndPoint(app, get_phone_book_records, update_phone_book_record, delete_phone_book_record)
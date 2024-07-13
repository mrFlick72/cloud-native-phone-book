import base64
import dataclasses
import datetime

from domain.PhoneBook import PhoneBook
from infrastructure.LocalThreadUserNameResolver import LocalThreadUserNameResolver

DATE_FORMAT = '%Y-%m-%d'


def fromDomainToRepresentations(phone_book_records: list[PhoneBook]):
    result = []
    for item in phone_book_records:
        result.append(fromDomainToRepresentation(item))
    return result


def fromDomainToRepresentation(phone_book_record: PhoneBook):
    user_name = LocalThreadUserNameResolver().get_user_name()
    item_as_dict = dataclasses.asdict(phone_book_record)
    item_as_dict["user_name"] = user_name
    item_as_dict["birth_date"] = item_as_dict["birth_date"].strftime(DATE_FORMAT)
    return item_as_dict


def fromRepresentationToDomain(contact_id, phone_book_record_dict):
    user_name = LocalThreadUserNameResolver().get_user_name()
    return PhoneBook(
        user_name=user_name,
        contact_name=contact_name(contact_id),
        phone_number=phone_book_record_dict["phone_number"],
        birth_date=datetime.datetime.strptime(phone_book_record_dict["birth_date"], DATE_FORMAT),
    )


def contact_name(contact_id):
    return base64.b64decode(contact_id).decode('utf-8')

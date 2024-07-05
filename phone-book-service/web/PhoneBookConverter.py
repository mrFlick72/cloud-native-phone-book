import dataclasses

from domain.PhoneBook import PhoneBook


def fromDomainToRepresentations(phone_book_records: list[PhoneBook]):
    plain_records = []
    for item in phone_book_records:
        plain_records.append(fromDomainToRepresentation(item))
    return plain_records


def fromDomainToRepresentation(phone_book_record: PhoneBook):
    asdict = dataclasses.asdict(phone_book_record)
    asdict["birth_date"] = asdict["birth_date"].strftime('%Y-%m-%d')
    return asdict

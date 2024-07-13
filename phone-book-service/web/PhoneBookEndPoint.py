import dataclasses
import json

from flask import Flask, request, jsonify

from domain import UserNameResolver
from domain.PhoneBook import GetPhoneBookRecords, SavePhoneBookRecord, DeletePhoneBookRecord
from web.PhoneBookConverter import fromDomainToRepresentations, fromRepresentationToDomain, contact_name


class PhoneBookEndPoint:

    def __init__(self,
                 app: Flask,
                 get_phone_book_records: GetPhoneBookRecords,
                 update_phone_book_record: SavePhoneBookRecord,
                 delete_phone_book_record: DeletePhoneBookRecord,
                 user_name_resolver: UserNameResolver
                 ):
        self.app = app
        self.user_name_resolver = user_name_resolver
        self.get_phone_book_records = get_phone_book_records
        self.update_phone_book_record = update_phone_book_record
        self.delete_phone_book_record = delete_phone_book_record

        app.add_url_rule("/phone-book", "get_phone_book_record_api", self.get_phone_book_record_api, methods=['GET'])
        app.add_url_rule("/phone-book/<contact_id>", "save_phone_book_record_api", self.save_phone_book_record_api,
                         methods=['PUT'])
        app.add_url_rule("/phone-book/<contact_id>", "delete_phone_book_record_api",
                         self.delete_phone_book_record_api, methods=['DELETE'])

    def get_phone_book_record_api(self):
        phone_book_records = self.get_phone_book_records.execute(self.user_name_resolver.get_user_name())
        plain_records = fromDomainToRepresentations(phone_book_records)

        return self.app.response_class(
            response=json.dumps(plain_records),
            status=200,
            content_type='application/json',
            mimetype='application/json'
        )

    def save_phone_book_record_api(self, contact_id):
        phone_book_repository = fromRepresentationToDomain(contact_id, json.loads(request.data))
        self.update_phone_book_record.execute(phone_book_repository)
        return self.app.response_class(status=204)

    def delete_phone_book_record_api(self, contact_id):
        self.delete_phone_book_record.execute(self.user_name_resolver.get_user_name(), contact_name(contact_id))
        return self.app.response_class(status=204)

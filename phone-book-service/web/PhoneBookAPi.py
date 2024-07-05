import dataclasses
import json

from flask import Flask, request

from domain.PhoneBook import GetPhoneBookRecords, SavePhoneBookRecord, DeletePhoneBookRecord


class PhoneBookAPi:

    def __init__(self,
                 app: Flask,
                 get_phone_book_records: GetPhoneBookRecords,
                 update_phone_book_record: SavePhoneBookRecord,
                 delete_phone_book_record: DeletePhoneBookRecord,
                 ):
        self.app = app
        self.get_phone_book_records = get_phone_book_records
        self.update_phone_book_record = update_phone_book_record
        self.delete_phone_book_record = delete_phone_book_record

        app.add_url_rule("/phone-book", "get_phone_book_record_api", self.get_phone_book_record_api, methods=['GET'])
        app.add_url_rule("/phone-book/<contact_id>", "save_phone_book_record_api", self.save_phone_book_record_api,
                         methods=['PUT'])
        app.add_url_rule("/phone-book/<contact_id>", "delete_phone_book_record_api",
                         self.delete_phone_book_record_api, methods=['DELETE'])

    def get_phone_book_record_api(self):
        phone_book_records = self.get_phone_book_records.execute("vvaudi")
        plain_records = []
        for item in phone_book_records:
            asdict = dataclasses.asdict(item)
            asdict["birth_date"] = asdict["birth_date"].strftime('%Y-%m-%d')
            plain_records.append(asdict)

        return self.app.response_class(
            response=json.dumps(plain_records),
            status=200,
            content_type='application/json',
            mimetype='application/json'
        )

    def save_phone_book_record_api(self, contact_id):
        # self.add_phone_book_record
        print(contact_id)
        print(request)
        return self.app.response_class(status=204)

    def delete_phone_book_record_api(self, contact_id):
        # self.add_phone_book_record
        print(contact_id)
        return self.app.response_class(status=204)

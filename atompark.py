import hashlib
import requests
import collections
import json


class SmsManager():
    def __init__(self, pub_key, secret_key, version="3.0"):
        self.pub_key = pub_key
        self.secret_key = secret_key
        self.version = version

    def __get_hashsum(self, **kwargs):
        m = hashlib.md5()
        m.update(
            "".join([v for k, v in collections.OrderedDict(sorted(kwargs.items())).items() if v]) + self.secret_key
        )
        return m.hexdigest()

    def __get_req_url(self, **kwargs):
        control_sum = self.__get_hashsum(version=self.version, key=self.pub_key, **kwargs)
        req_url = "http://atompark.com/api/sms/3.0/{action}?" \
                  "key={pub_key}&" \
                  "sum={control_sum}".format(action=kwargs.get("action"),
                                             pub_key=self.pub_key,
                                             control_sum=control_sum)
        for key, value in kwargs.items():
            if key == "action" or not value:
                continue
            req_url += "&{key}={value}".format(key=key, value=value)

        print req_url
        return req_url

    def make_api_req(self, **kwargs):
        return requests.get(self.__get_req_url(**kwargs)).json()

    def add_address_book(self, name, description=None):
        return self.make_api_req(action="addAddressbook", name=name, description=description)

    def del_address_book(self, id_address_book):
        return self.make_api_req(action="delAddressbook", idAddressBook=id_address_book)

    def edit_address_book(self, id_address_book, new_name, new_description=None):
        return self.make_api_req(action="editAddressbook", idAddressBook=id_address_book, newName=new_name,
                                 newDescr=new_description)

    def get_address_book(self, id_address_book=None, offset=0):
        return self.make_api_req(action="getAddressbook", idAddressBook=id_address_book, offset=offset)

    def search_address_book(self, search_fields, offset=0):
        return self.make_api_req(action="searchAddressBook", searchFields=json.dumps(search_fields), offset=offset)

    def add_phone_to_address_book(self, id_address_book, phone, variables=None):
        return self.make_api_req(action="addPhoneToAddressBook", idAddressBook=id_address_book, phone=phone,
                                 variables=variables)

    def add_phones_to_address_book(self, id_address_book, data):
        return self.make_api_req(action="addPhoneToAddressBook", idAddressBook=id_address_book, data=data)

    def get_phone_from_address_book(self, id_address_book=None, id_phone=None, phone=None, offset=0):
        return self.make_api_req(action="getPhoneFromAddressBook", idAddressBook=id_address_book, idPhone=id_phone,
                                 phone=phone, offset=offset)

    def send_sms(self, sender, text, phone, datetime=None, sms_lifetime=0):
        return self.make_api_req(action="sendSMS", sender=sender, text=text,
                                 phone=phone, datetime=datetime, sms_lifetime=sms_lifetime)
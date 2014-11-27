#!/usr/bin/env python
import settings
from flask import Flask
from atompark import SmsManager
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)


@manager.option('-n', '--name', dest='name', default=None)
@manager.option('-d', '--description', dest='description', default="")
def add_address_book(name, description):
    smsmanager = SmsManager(settings.SMS_PUB_KEY, settings.SMS_SECRET_KEY, settings.SMS_API_VERSION)
    print smsmanager.add_address_book(name, description)


@manager.option('-i', '--id', dest='id_address_book', default=None)
def del_address_book(id_address_book):
    smsmanager = SmsManager(settings.SMS_PUB_KEY, settings.SMS_SECRET_KEY, settings.SMS_API_VERSION)
    print smsmanager.del_address_book(id)


@manager.option('-i', '--id', dest='id_address_book')
@manager.option('-n', '--name', dest='name')
@manager.option('-d', '--description', dest='description', default=None)
def edit_address_book(id_address_book, name, description):
    smsmanager = SmsManager(settings.SMS_PUB_KEY, settings.SMS_SECRET_KEY, settings.SMS_API_VERSION)
    print smsmanager.edit_address_book(id_address_book, name, description)


@manager.option('-i', '--id', dest='id_address_book', default=None)
@manager.option('-o', '--offset', dest='offset', default=0)
def get_address_book(id_address_book=None, offset=0):
    smsmanager = SmsManager(settings.SMS_PUB_KEY, settings.SMS_SECRET_KEY, settings.SMS_API_VERSION)
    print smsmanager.get_address_book(id_address_book, offset)


@manager.option('-s', '--search_fields', dest='search_fields')
@manager.option('-o', '--offset', dest='offset', default=0)
def search_address_book(search_fields, offset=0):
    smsmanager = SmsManager(settings.SMS_PUB_KEY, settings.SMS_SECRET_KEY, settings.SMS_API_VERSION)
    print smsmanager.search_address_book(search_fields, offset)


@manager.option('-i', '--id', dest='id_address_book')
@manager.option('-p', '--phone', dest='phone')
@manager.option('-v', '--variables', dest='variables', default=None)
def add_phone_to_address_book(id_address_book, phone, variables):
    smsmanager = SmsManager(settings.SMS_PUB_KEY, settings.SMS_SECRET_KEY, settings.SMS_API_VERSION)
    print smsmanager.add_phone_to_address_book(id_address_book, phone, variables)


@manager.option('-i', '--id', dest='id_address_book')
@manager.option('-d', '--data', dest='data')
def add_phones_to_address_book(id_address_book, data):
    smsmanager = SmsManager(settings.SMS_PUB_KEY, settings.SMS_SECRET_KEY, settings.SMS_API_VERSION)
    print smsmanager.add_phones_to_address_book(id_address_book, data)


@manager.option('-a', '--id-address-book', dest='id_address_book', default=None)
@manager.option('-i', '--id-phone', dest='id_phone', default=None)
@manager.option('-p', '--phone', dest='phone', default=None)
@manager.option('-o', '--offset', dest='offset', default=0)
def get_phone_from_address_book(id_address_book, id_phone, phone, offset):
    smsmanager = SmsManager(settings.SMS_PUB_KEY, settings.SMS_SECRET_KEY, settings.SMS_API_VERSION)
    print smsmanager.get_phone_from_address_book(id_address_book, id_phone, phone, offset)


@manager.option('-s', '--sender', dest='sender')
@manager.option('-t', '--text', dest='text')
@manager.option('-p', '--phone', dest='phone')
@manager.option('-d', '--datetime', dest='datetime', default=None)
@manager.option('-l', '--lifetime', dest='sms_lifetime', default=0)
def send_sms(sender, text, phone, datetime, sms_lifetime):
    smsmanager = SmsManager(settings.SMS_PUB_KEY, settings.SMS_SECRET_KEY, settings.SMS_API_VERSION)
    print smsmanager.send_sms(sender, text, phone, datetime, sms_lifetime)

if __name__ == "__main__":
    manager.run()
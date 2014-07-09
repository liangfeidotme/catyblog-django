__author__ = 'lyndon'
# -*- coding: utf-8 -*-
from pymongo import MongoClient

_client = MongoClient('localhost', 27017)
_db = _client.note_db


def insert_issue():
    test_collection = _db.test_collection
    test_collection.insert(
        {
            'tag': 'japanese',
            'note': u'你是谁',
        })


def get_issue():
    return _db.test_collection.find_one()


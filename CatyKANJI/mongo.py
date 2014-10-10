__author__ = 'lyndon'

import os
import shutil
import json

from pymongo import MongoClient
from catyblog.settings import KANJI_RES_ROOT


class KanjiMongo:
    DATA_BASE = "catykanji"
    PENDING_DIR = os.path.join(KANJI_RES_ROOT, "pending")
    FINISHED_DIR = os.path.join(KANJI_RES_ROOT, "finished")

    def __init__(self):
        self._client = MongoClient()
        self._db = self._client[self.DATA_BASE]

    def get_kanji(self):
        # check pending dir to see if there's any file
        self.check_update()
        return self._db.kanji.find()

    def insert_kanji(self, kanji):
        self._db.kanji.insert(kanji)

    def write_to_db(self, path):
        with open(path) as my_file:
            self._db.kanji.insert(json.loads(my_file.read()))

    def check_update(self):
        for (path, dirs, files) in os.walk(self.PENDING_DIR):
            for file in files:
                self.write_to_db(os.path.join(path, file))

                # move sync-over file into 'finished' directory
                shutil.move(os.path.join(path, file), os.path.join(self.FINISHED_DIR, file))

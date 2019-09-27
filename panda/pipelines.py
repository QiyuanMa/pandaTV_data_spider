# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from datetime import datetime


class PandaIdPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.count = 0

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        d = dict(item)
        colletion_scrapy = self.db['panda_scrapy']
        collection_id = self.db['panda_id']
        collection_room = self.db['panda_room']
        colletion_scrapy.insert_one(d)
        d.pop('_id')

        result = collection_id.update_one({'id': d.get('id')}, {'$set': d})
        if result.matched_count == 0:
            self.count += 1
            collection_id.insert_one(d)
            collection_room.insert_one({'id': d.get('id')})
        return item

    def close_spider(self, spider):
        record = self.db['record']
        record.insert_one({'tid': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'inc': self.count})
        self.client.close()
        print('新增用户', self.count)


class PandaRoomPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        d = dict(item)
        self.db['panda_room'].update_one({'id': d.get('id')}, {'$set': d})
        return item

    def close_spider(self, spider):
        self.client.close()

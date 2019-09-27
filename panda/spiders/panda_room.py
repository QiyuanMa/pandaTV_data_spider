# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode, parse_qsl
import pymongo
from panda.items import PandaRoomItem
from time import sleep
import json


class PandaRoomSpider(scrapy.Spider):
    name = 'panda_room'
    allowed_domains = ['https://www.panda.tv']
    start_urls = ['http://https://www.panda.tv/']

    def start_requests(self):
        fans_url = 'https://www.panda.tv/room_followinfo?'
        fans_data = {
            'token': '',
            '_': '1540299504941'
        }

        rank_url = 'https://grank.panda.tv/room_{}_rank?'
        rank_data = {
            'token': '',
            '_': '1540299504941'
        }

        pop_url = 'https://www.panda.tv/api_room_v3?token=&'
        pop_data = {
            '_': '1541291921326',
            'time': '1541291841',
            'param': {"room_type": "1", "person_num": 0},
            'sign': ''
        }
        para = '{"roomid":"{}","hostid":"{}","room_key":"{}","room_type":"1","person_num":0}'
        client = pymongo.MongoClient('localhost:27017')
        db = client['PandaTV']
        collection = db['panda_id']
        result = collection.find()
        for i in result:
            fans_data['roomid'] = i.get('id')
            rank_data['anchor_id'] = i.get('rid')
            rank_data['room_id'] = i.get('id')
            pop_data['hostid'] = i.get('rid')
            pop_data['roomid'] = i.get('id')
            pop_data['roomkey'] = i.get('room_key')
            pop_data['param']['roomid'], pop_data['param']['hostid'], pop_data['param']['roomkey'] = i.get('id'), i.get(
                'rid'), i.get('room_key')
            # yield scrapy.Request(fans_url + urlencode(fans_data), callback=self.fans_parse)
            # yield scrapy.Request(rank_url.format('total') + urlencode(rank_data), callback=self.total_rank_parse)
            # yield scrapy.Request(rank_url.format('weekly') + urlencode(rank_data), callback=self.weekly_rank_parse)
            yield scrapy.Request(pop_url + urlencode(pop_data), callback=self.popularity_parse, dont_filter=True)
            print(pop_url + urlencode(pop_data))

    def fans_parse(self, response):
        j = json.loads(response.text)
        data = dict(parse_qsl(response.url))
        item = PandaRoomItem()
        item['id'] = data.get('roomid')
        item['fans'] = j.get('data').get('fans')
        yield item

    def total_rank_parse(self, response):
        j = json.loads(response.text)
        data = dict(parse_qsl(response.url))
        item = PandaRoomItem()
        item['id'] = data.get('room_id')
        ds = []
        for i in j.get('data').get('top10'):
            ds.append({
                'rid': i.get('uid'),
                'nickname': i.get('nickname'),
                'score': i.get('score')
            })
        item['total_rank'] = ds
        yield item

    def weekly_rank_parse(self, response):
        j = json.loads(response.text)
        data = dict(parse_qsl(response.url))
        item = PandaRoomItem()
        item['id'] = data.get('room_id')
        ds = []
        for i in j.get('data').get('top10'):
            ds.append({
                'rid': i.get('uid'),
                'nickname': i.get('nickname'),
                'score': i.get('score')
            })
        item['weekly_rank'] = ds
        yield item

    def popularity_parse(self, response):
        j = json.loads(response.text)
        data = dict(parse_qsl(response.url))
        item = PandaRoomItem()
        item['id'] = data.get('roomid')
        item['popularity'] = j.get('data').get('roominfo').get('person_time')
        yield item

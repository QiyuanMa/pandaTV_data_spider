# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode, parse_qsl
from datetime import datetime
from panda.items import PandaIDItem
import json


class PandaIdSpider(scrapy.Spider):
    name = 'panda_id'
    allowed_domains = ['https://www.panda.tv']
    start_urls = ['http://https://www.panda.tv/']

    def start_requests(self):
        self.base_url = 'https://www.panda.tv/ajax_sort?token=&'
        cate = [
            'lol', 'gbaby', 'fortnite', 'yzdr', 'hwzb', 'food', 'voice', 'zhuji', 'hearthstone', 'overwatch', 'dota1',
            'dota2', 'roe', 'war3', 'pubg', 'legends', 'cf', 'dnf', 'scum', 'nsh', 'hyplus', 'wow', 'jxol3', 'tymyd',
            'gjqtol', 'popkart', 'mxd2', 'qipai', 'majiang', 'doudizhu', 'billiards', 'wx', 'spg', 'bf', 'fifa',
            'hjjd', 'wegame', 'csgo', 'mh', 'fifamobile', 'cod15', 'heroes', 'nba2kol2', 'starcraft', 'boardgames',
            'artifact', 'ftg', 'mc', 'liufang', 'diablo3', 'wy', 'qqfc', 'shoot', 'kingglory', 'dwrg', 'newgames',
            'fishes', 'cjzc', 'pubgm', 'zjz', 'sycj', 'zhcj', 'mhxy', 'fcsy', 'pubgmo', 'ciyuan', 'werewolf', 'girl',
            'music', 'sanguo', 'cartoon', 'sdyxl', 'ztyx', 'naruto', 'technology', 'wenwanjianshang', 'joy',
            'indiegame', 'cfm', 'moba', 'sdsxs', 'qqdzz', 'frxy', 'mobilegame'
        ]
        data = {
            'pagenum': 120,
            'pageno': 1,
            'order': 'top',
            '_': '1539333209583'
        }
        for c in cate:
            data['classification'] = c
            yield scrapy.Request(self.base_url + urlencode(data), self.parse)

    def parse(self, response):
        j = json.loads(response.text)
        ls = j.get('data').get('items')
        if len(ls) > 0:
            for i in ls:
                item = PandaIDItem()
                item['tid'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                item['classification'] = i.get('classification')
                item['id'] = i.get('id')
                item['rid'] = i.get('userinfo').get('rid')
                item['nickname'] = i.get('userinfo').get('nickName')
                item['person_num'] = int(i.get('person_num'))
                item['ticket_rank_info'] = i.get('ticket_rank_info')
                item['host_level_info'] = i.get('host_level_info')
                item['room_key'] = i.get('room_key')
                yield item
            d = dict(parse_qsl(response.url))
            d['pageno'] = int(d['pageno']) + 1
            yield scrapy.Request(self.base_url + urlencode(d), callback=self.parse, dont_filter=True)

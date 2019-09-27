# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class PandaIDItem(Item):
    tid = Field()
    classification = Field()
    id = Field()
    room_key = Field()
    rid = Field()
    nickname = Field()
    person_num = Field()
    ticket_rank_info = Field()
    host_level_info = Field()


class PandaRoomItem(Item):
    id = Field()
    fans = Field()
    popularity = Field()
    total_rank = Field()
    weekly_rank = Field()

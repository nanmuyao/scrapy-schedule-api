# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GremonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CoinMarketCapItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    symbol = scrapy.Field()
    rank = scrapy.Field()
    price_usd = scrapy.Field()
    price_btc = scrapy.Field()
    h24_volume_usd = scrapy.Field()
    market_cap_usd = scrapy.Field()
    available_supply = scrapy.Field()
    total_supply = scrapy.Field()
    percent_change_1h = scrapy.Field()
    percent_change_24h = scrapy.Field()
    percent_change_7d = scrapy.Field()
    last_updated = scrapy.Field()
    # CNY
    price_cny = scrapy.Field()
    h24_volume_cny = scrapy.Field()
    market_cap_cny = scrapy.Field()
    # ETH
    price_eth = scrapy.Field()
    # High and Low
    h24_highest_usd = scrapy.Field()
    h24_lowest_usd = scrapy.Field()

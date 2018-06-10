# -*- coding: utf-8 -*-
import scrapy
import logging
import json
from scrapy.http import Request
from gremon.items import CoinMarketCapItem


class CoinmarketcapSpider(scrapy.Spider):
    name = 'coinmarketcap'
    allowed_domains = ['api.coinmarketcap.com']
#    start_urls = ['http://www.coinmarketcap.com/']
    start_urls = ['https://api.coinmarketcap.com/v1/ticker/?']

    def __init__(self, setting):
        self.request_count = 0
        self.url = 'https://api.coinmarketcap.com/v1/ticker/?'
        logging.warning("当前的配置")

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings)

    def parse(self, response):
        #print("response", response.text
        content = response.text
        try:
            print(len(content))
        except:
            print("请求出错了")
        
        self.request_count = self.request_count + 1
        for index in range(100000):
            yield Request(url=self.url, callback=self.parse_earch, dont_filter=True)

    def parse_earch(self, response):
        self.request_count = self.request_count + 1
        logging.warning('request_count=%d', self.request_count)
        json_response = json.loads(response.text)
        if not (len(json_response) == 1 and
                'error' in json_response[0]):
            for json_obj in json_response:
                item = CoinMarketCapItem()
                item['id'] = json_obj['id']
                item['name'] = json_obj['name']
                item['symbol'] = json_obj['symbol']
                item['rank'] = json_obj['rank']
                item['price_usd'] = json_obj['price_usd']
                item['price_btc'] = json_obj['price_btc']
                item['h24_volume_usd'] = json_obj['24h_volume_usd']
                item['market_cap_usd'] = json_obj['market_cap_usd']
                item['available_supply'] = json_obj['available_supply']
                item['total_supply'] = json_obj['total_supply']
                item['percent_change_1h'] = json_obj['percent_change_1h']
                item['percent_change_24h'] = json_obj['percent_change_24h']
                item['percent_change_7d'] = json_obj['percent_change_7d']
                item['last_updated'] = json_obj['last_updated']
            yield item


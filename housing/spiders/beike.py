import scrapy
from scrapy.linkextractors import LinkExtractor
import json


def seed():
    return [
        'https://m.ke.com/city/'
    ]


class Beike(scrapy.Spider):
    name = 'beike'
    start_urls = seed()

    def parse(self, response):
        links = LinkExtractor(restrict_css='div.city_block_item > a').extract_links(response)
        self.logger.info('URL: %s,  %s CITY ', response.url, len(links))
        for link in links[0:1]:
            url = link.url
            city_name = link.text
            yield scrapy.Request(url, meta={"city_name": city_name}, callback=self.parse_city)

    def parse_city(self, response):
        self.logger.info("CITY: %s %s", response.url, response.meta)

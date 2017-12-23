# -*- coding: utf-8 -*-
import scrapy
import random
from spd.items import SpdItem
import os
class SimpleDesktopSpider(scrapy.Spider):
    name = 'spd'
    browse_url = 'http://simpledesktops.com/browse/'
    rooturl = "http://simpledesktops.com"
    
    def __init__(self):
        randompage = random.randint(1,40)
        self.start_urls = [self.browse_url + str(randompage)]

    def parse(self, response):
        wallpapers = response.xpath('//div[@class="desktop"]')
        select_paper = wallpapers[random.randint(0,len(wallpapers) - 1)]
        url = select_paper.xpath('./a/@href').extract_first()
        next_url = self.rooturl + url
        yield scrapy.Request(next_url, callback=self.parse_next)

    def parse_next(self, response):
        image = response.xpath('//div[@class="desktop"]/a/@href').extract_first()
        str_start = response.url.rfind('/',0,len(response.url) - 2)
        filename = response.url[str_start + 1:len(response.url) - 1] + ".png"
        item = SpdItem()
        item['image_urls'] = self.rooturl + image 
        item['image_name'] = filename
        yield item 
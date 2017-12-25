# -*- coding: utf-8 -*-
import scrapy
import random
from spd.items import SpdItem
import os
import re
class WallhavenSpider(scrapy.Spider):
    name = 'wallhaven'
    browse_url = 'https://alpha.wallhaven.cc/toplist?page='
    rooturl = "https://alpha.wallhaven.cc"
    
    def __init__(self):
        randompage = random.randint(1,148)
        self.start_urls = [self.browse_url + str(randompage)]

    def parse(self, response):
        wallpapers = response.xpath('//a[@class="preview"]')
        select_paper = wallpapers[random.randint(0,len(wallpapers) - 1)]
        url = select_paper.xpath('./@href').extract_first()
        # print("nexturl %s"%url)
        yield scrapy.Request(url, callback=self.parse_next)

    def parse_next(self, response):
        image = response.xpath('//img[@id="wallpaper"]/@src').extract_first()
        image_urls = "https:" + image
        title = response.xpath('//title/text()').extract_first()
        select_title = re.search('#.*?,',title).group()
        filename = select_title[1:-1] + str(random.randint(1,100)) + image_urls[-4:]
        filename = filename.replace(' ','')
        # print("filename%s, image_url %s" % (filename, image_urls))
        item = SpdItem()
        item['image_urls'] = image_urls 
        item['image_name'] = filename
        yield item
# -*- coding: utf-8 -*-
import scrapy
import random
from spd.items import SpdItem
import os
class SimpleDesktopSpider(scrapy.Spider):
    name = 'hdwallpapers'
    browse_url = 'https://www.hdwallpapers.in/2560x1600_wide-wallpapers-r/page/'
    rooturl = "https://www.hdwallpapers.in/"
    
    def __init__(self):
        randompage = random.randint(1,500)
        self.start_urls = [self.browse_url + str(randompage)]

    def parse(self, response):
        wallpapers = response.xpath('//div[@class="thumb"]')
        select_paper = wallpapers[random.randint(0,len(wallpapers) - 1)]
        url = select_paper.xpath('./a/@href').extract_first()
        next_url = self.rooturl + url
        yield scrapy.Request(next_url, callback=self.parse_next)

    def parse_next(self, response):
        image = response.xpath('//div[@class="wallpaper-resolutions"]/a[@title="2560 x 1600"]/@href').extract_first()
        str_start = image.rfind('/',0,len(image) - 2)
        filename = image[str_start + 1:len(image)]
        item = SpdItem()
        item['image_urls'] = self.rooturl + image 
        item['image_name'] = filename
        yield item 
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
class SpdPipeline(object):
    def process_item(self, item, spider):
        if item['image_urls']:
            cmd = "wget " + item['image_urls'] + " -q -O " + item['image_name'] + " &&" + " ./setbg " + item['image_name']
            os.system(cmd)
            rm_img = 'rm ' + item['image_name']
            os.system(rm_img)
        return item


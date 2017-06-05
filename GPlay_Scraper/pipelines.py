# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
from scrapy.exceptions import DropItem
#from scrapy.exporters import JsonItemExporter
import sqlite3
class GplayScraperPipeline(object):
    def __init__(self):
        #self.file = open("Apps.json", 'wb')
        #elf.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        #self.exporter.start_exporting()
        self.conn = sqlite3.connect('Spiders.db')
        self.cursor = self.conn.cursor() 
        self.cursor.execute('CREATE TABLE IF NOT EXISTS AppData(app text);')
        self.conn.commit()

    def close_spider(self, spider):
        #self.exporter.finish_exporting()
        #self.file.close()
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        #self.exporter.export_item(item)
        if(item['price'] == 'Free'):
        	self.cursor.execute('INSERT INTO AppData(app) VALUES (?)', (item['appid'],))
        	self.conn.commit()
        	return item
        else:
        	raise DropItem('App not Free %s' % item)


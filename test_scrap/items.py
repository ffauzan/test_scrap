# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field  

class First_scrapyItem(scrapy.Item): 
   nama_produk = scrapy.Field() 
   harga_produk = scrapy.Field() 
   url_produk = scrapy.Field() 
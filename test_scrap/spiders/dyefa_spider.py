import scrapy
from scrapy.item import Item 

class firstSpider(scrapy.Spider): 
   name = "dyefa_spider" 
   allowed_domains = ["dyefa.com"] 
   
   start_urls = [ 
      "http://www.dyefa.com/led-monitor?sort=date_modified-DESC&page=1",
      "http://www.dyefa.com/led-monitor?sort=date_modified-DESC&page=2",
      "http://www.dyefa.com/led-monitor?sort=date_modified-DESC&page=3",
      "http://www.dyefa.com/led-monitor?sort=date_modified-DESC&page=4",
      "http://www.dyefa.com/led-monitor?sort=date_modified-DESC&page=5"
   ]  
   def parse(self, response):
       harga = response.xpath("//div[@class='pricenew']/text()").extract()
       nama = response.xpath('//div[@class="fixed"]/a/text()').extract()
       url = response.xpath("//div[@class='thumbnail']/a/@href").extract()
       for nama_produk, harga_produk, url_produk in zip(nama,harga,url):

           harga_produk = harga_produk.encode('ascii', 'ignore')
           nama_produk =  nama_produk.encode('ascii', 'ignore')

           yield{
               'nama_produk': nama_produk,
               'harga_produk': harga_produk,
               'url_produk': url_produk,
           }
           #print nama, harga, url  

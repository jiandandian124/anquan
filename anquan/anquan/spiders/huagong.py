import scrapy
from anquan.items import AnquanItem
# scrapy crawl huagong -o huagong.csv
# scrapy crawl huagong -o huagong.json

class HuagongSpider(scrapy.Spider):
    name = 'huagong'
    allowed_domains = ['safehoo.com']
    start_urls = ['http://www.safehoo.com/NewsSpecial/Particular/Index.shtml']

    def parse(self, response):
        #/ html / body / div[8] / div[1] / div[3] / li[1]
        lie = response.xpath('/html/body/div[5]/div[1]/div[3]/li')
        for tiao in lie:
            url = tiao.xpath('./a/@href').extract()[0]
            u = response.urljoin(url)
            yield scrapy.Request(url=u, callback=self.parse_s)
        next = response.xpath('/html/body/div[5]/div[1]/div[4]/span/a[7]/@href').extract()[0]
        ur = response.urljoin(next)
        yield scrapy.Request(url=ur, callback=self.parse)
        
    def parse_s(self, response):

        item = AnquanItem()
        text = response.xpath('/html/body/div[8]/div[1]/div[1]/div[2]/div[1]/div[4]/p/text()').extract()

        if text:
            item['text'] = text
            item['label'] = '特种设备'
        else:
            item['text'] = '无'
            item['label'] = '特种设备'
        yield item
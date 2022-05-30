import scrapy
from sigu.items import SiguItem


# scrapy crawl huagong -o huagong.csv
# scrapy crawl huagong -o huagong.json

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['safehoo.com']
    start_urls = ['http://www.safehoo.com/NewsSpecial/Coal/Index.shtml']

    def parse(self, response):
        lie = response.xpath('/html/body/div[5]/div[1]/div[3]/li')
        for tiao in lie:
            url = tiao.xpath('./a/@href').extract()[0]
            u = response.urljoin(url)
            yield scrapy.Request(url=u, callback=self.parse_s)

        next = response.xpath('/html/body/div[5]/div[1]/div[4]/span/a[9]/@href').extract()[0]
        ur = response.urljoin(next)
        yield scrapy.Request(url=ur, callback=self.parse)

    def parse_s(self, response):

        item = SiguItem()
        text = response.xpath('/html/body/div[8]/div[1]/div[1]/div[2]/div[1]/div[4]/p/text()').extract()

        if text:
            item['label'] = '矿山事故'
            item['text'] = text
        else:
            item['label'] = '矿山事故'
            item['text'] = '无'
        yield item


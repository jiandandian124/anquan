import scrapy
from anquan.items import AnquanItem
# scrapy crawl huagong -o huagong.csv
# scrapy crawl huagong -o huagong.json

class HuagongSpider(scrapy.Spider):
    name = 'huagong'
    allowed_domains = ['safehoo.com']
    start_urls = ['http://www.safehoo.com/Manage/Trade/Chemical/List_51.shtml']

    def parse(self, response):
        
        lie = response.xpath('/html/body/div[8]/div[1]/div[3]/li')       
        for tiao in lie:           
            leixing = tiao.xpath('./text()').extract()
            if leixing == ['\n[ 文章]\n'] :
                url = tiao.xpath('./a/@href').extract()[0]
                item = AnquanItem()
                item['url'] = url
                u = response.urljoin(url)
                yield scrapy.Request(url = u,callback = self.parse_s)                                
            else :                                
                print('1')
        
        next = response.xpath('//*[@id="pe100_page_通用信息列表_列表式"]/a[9]/@href').extract()[0]
        ur = response.urljoin(next)
        yield scrapy.Request(url=ur, callback=self.parse)
        
    def parse_s(self,response):

        item = AnquanItem()
        title = response.xpath('//*[@id="prt1"]/h1/span/text()').extract()[0]
        text = response.xpath('//*[@id="prt2"]/div/p/text()').extract()
        tags = response.xpath('/html/body/div[8]/div[1]/div[3]/div[1]/li/span/a/text()').extract()
        concern = response.xpath('/html/body/div[8]/div[1]/div[3]/div[2]/li/a/text()').extract()

        if text:
            item['text'] = text
        else:
            item['text'] = '无'    
        
        if tags:
            item['tags'] = tags
        else:
            item['tags'] = '无'
        
        if concern:
            item['concern'] = concern
        else:
            item['concern'] = '无'

        if title:
            item['title'] = title
        else:
            item['title'] = '无'
        yield item
    
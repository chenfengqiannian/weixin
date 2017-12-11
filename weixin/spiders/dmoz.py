# coding=utf-8
from scrapy.spiders import Spider
from weixin.items import WeixinItem
import scrapy



class DmozSpider(Spider):
    name = "dmoz"
    count = 0

    COOKIES_ENABLED = False
    handle_httpstatus_list = [403,302]
    start_urls = [



    ]

    def __init__(self, listlen=2):
        super(DmozSpider, self).__init__()
        for i in range(1,14):
            url="http://weixin.sogou.com/pcindex/pc/pc_0/%d.html"%i
            self.start_urls.append(url)






    def parse(self, response):
        print response.body

        for i in response.css("li"):

            item=WeixinItem()
            item['title'] = i.css("h3 a::text").extract_first()
            item["content"]=i.css("p::text").extract_first()
            item['url']=i.css("a::attr(href)").extract_first()
            print item
            yield item




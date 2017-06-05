import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from GPlay_Scraper.items import GplayScraperItem
from scrapy.selector import HtmlXPathSelector



class GPlaySpider(CrawlSpider):
    name = 'google'
    allowed_domains = ['play.google.com']
    start_urls = ['https://play.google.com/store/apps/details?id=com.onemangamestudio.MeditationGame']
    rules = [Rule(LinkExtractor(allow=("https://play\.google\.com/store/apps/details",)), callback='parse_app', follow=True),]

    def parse_app(self, response):
        item = GplayScraperItem()
        for object_per in response.xpath('//div[@class="card no-rationale square-cover apps small"]/div[@class="card-content id-track-click id-track-impression"]'):
            url =  object_per.xpath('div[@class="details"]/a/@href')[0].extract()
            price = object_per.xpath('div[@class="details"]/div[@class="subtitle-container"]/span/span[2]/button/span/text()')[0].extract()
            #url = url.strip()
            #price = price.strip()
            item['appid'] = url[23:]
            item['price'] = price
            yield item
'''
Created on 2013-6-24

@author: yanggx
'''

from django.core.management import setup_environ
from Django_Learn import settings
setup_environ(settings)

# import scrapy stuff
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from scrapy.utils.response import get_base_url

class Lawson(CrawlSpider):
    name = "Lawson"
    allowed_domains = ['lawson.com.cn']
    start_urls = ['http://www.lawson.com.cn/shops']
    rules = (Rule(SgmlLinkExtractor(allow=r'list\?area_id=\d+', tags='a'), callback='parse_lawson'))
    
    
    def parse_lawson(self, respone):
        hxs = HtmlXPathSelector(respone)
        store_selectors = hxs.select('//div[@class="ShopList"]/table/tr')[1:]
        
    
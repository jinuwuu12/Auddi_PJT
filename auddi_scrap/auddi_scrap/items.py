# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AuddiScrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class kukminScrapItem(scrapy.Item):
    source = scrapy.Field()
    title = scrapy.Field()
    date  = scrapy.Field()
    url   = scrapy.Field()
    
    
class dcinsideScrapItem(scrapy.Item):
    source         = scrapy.Field()
    gall_count     = scrapy.Field()
    gall_recommend = scrapy.Field()
    gall_num       = scrapy.Field()
    gall_tit       = scrapy.Field()
    gall_writer    = scrapy.Field()
    
    
class bobaeCommunityItem(scrapy.Item):
    gall_source = scrapy.Field()
    gall_title = scrapy.Field()
    gall_url   = scrapy.Field()
    gall_count = scrapy.Field()
    gall_benz_comment  = scrapy.Field()
    gall_audi_comment  = scrapy.Field()
    gall_bmw_comment   = scrapy.Field()
    
    
    
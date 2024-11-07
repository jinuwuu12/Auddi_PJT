import scrapy
import scrapy.resolver
from auddi_scrap.items import kukminScrapItem

class CommunitySpider(scrapy.Spider):
    name = "communityCrwaler"
    # 여러가지 사이트에서 크롤링 하는경우
    def start_requests_sports(self):
         for i in range(1,2,1):
             yield scrapy.Request('https://www.kmib.co.kr/article/list.asp?sid1=ens&page=%d' % i, self.parse_kukmin_sports)
            #  yield scrapy.Request('https://www.kmib.co.kr/article/list.asp?sid1=eco&page=%d' % i, self.parse_kukmin_economy)
 
        
    def parse_kukmin_sports(self, response):
        for link in response.css('.card.flex_aifs.flex_xsaicn.cgap_lg4.cgap_xs2'):
            item = kukminScrapItem()
            item['source'] = '스포츠/연예'
            item['title']  = link.css('.tit.fs_lg20.fs_xs16.fw_lgmd.lh_lg15 a::text').extract()[0]
            item['date']   = link.css('.date.gray500.fs_lg14.fw_lgrg::text').get()
            item['url']    = link.css('.tit.fs_lg20.fs_xs16.fw_lgmd.lh_lg15 a::attr(href)').get()
            
            print('='*50)
            
            yield item

    # def parse_kukmin_economy(self, response):
    #     for link in response.css('.nws_list.flex.flex_fw.flex_aifs.rgap_lg6.rgap_xs4'):
    #         item = kukminScrapItem()
    #         item['source'] = '경제'
    #         item['title']  = link.css('.tit.fs_lg20.fs_xs16.fw_lgmd.lh_lg15 a::text').extract()[0]
    #         item['date']   = link.css('.date.gray500.fs_lg14.fw_lgrg::text').get()
    #         item['url']    = link.css('.tit.fs_lg20.fs_xs16.fw_lgmd.lh_lg15 a::attr(href)').get()
            
    #         yield item
            
    
import scrapy
from auddi_scrap.items import bobaeCommunityItem

class newCrawlSpider(scrapy.Spider):
    name = 'bobaeCrawl'
    
    def start_requests(self):
        for i in range(1, 10, 1):
            yield scrapy.Request(
                f'https://www.bobaedream.co.kr/list?code=import&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={i}',
                callback=self.parse_bobae_car,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
            )
            
    def parse_bobae_car(self, response):
            for link in response.xpath('//tr[@itemscope][@itemtype="http://schema.org/Article"]'):
                # print(link)
                item = bobaeCommunityItem()
                
                item['gall_source'] = '수입차 커뮤니티'
                item['gall_title']  = link.css('.pl14 a::text').getall()[0]
                # item['gall_count']  = link.css['.count::text'].get()
                
                print('='*80)
                
                yield item
            
            

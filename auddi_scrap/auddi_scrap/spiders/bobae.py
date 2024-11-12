import scrapy
from auddi_scrap.items import bobaeCommunityItem

class newCrawlSpider(scrapy.Spider):
    name = 'bobaeCrawl'
    
    def start_requests(self):
        for i in range(1, 2, 1):
            yield scrapy.Request(
                f'https://www.bobaedream.co.kr/list?code=import&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={i}',
                callback=self.parse_bobae_car,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
            )
            
    def parse_bobae_car(self, response):
            comment_benz = []
            for link in response.xpath('//tr[@itemscope][@itemtype="http://schema.org/Article"]'):
                # print(link)
                item = bobaeCommunityItem()
                
                item['gall_source']  = '수입차 커뮤니티'
                item['gall_title']   = link.css('.pl14 a::text').getall()[0]
                item['gall_url']     = link.css('a.bsubject::attr(href)').get()
                
                #######################################################
                
                comment_benz.append(link.css('a.bsubject::attr(href)').get())
                
                for commentLink in comment_benz:
                    full_url = 'https://www.bobaedream.co.kr' + commentLink
                    yield scrapy.Request(full_url, callback=self.parse_takeComment)
                
                print('='*80)
                
                yield item
    

    def parse_takeComment(self, response):
        item = bobaeCommunityItem()
        
        item['gall_benz_comment'] = response.css('.commentlistbox dd::text').get()
        
        
        yield item
        
        
        
            

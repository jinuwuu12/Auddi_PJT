import scrapy
from auddi_scrap.items import dcinsideScrapItem

class newCrawlSpider(scrapy.Spider):
    name = 'dcinsideCrawl'
    
    def start_requests(self):
        for i in range(1, 2, 1):
            yield scrapy.Request(
                f'https://gall.dcinside.com/board/lists/?id=dcbest&page={i}&_dcbest=1',
                callback=self.parse_nowBest,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
            )
            
    def parse_nowBest(self, response):
        for link in response.css('.ub-content.us-post.thum'):
            item = dcinsideScrapItem()
            item['source']         = '실베게시판'
            item['gall_num']       = link.css('.gall_num::text').get()
            item['gall_tit']       = link.css('.gall_tit.ub-word a::text').getall()
            item['gall_tit']       = item['gall_tit'][-1]
            item['gall_writer']    = link.css('.nickname.in em::text').get()
            item['gall_count']     = link.css('.gall_count::text').get()
            item['gall_recommend'] = link.css('.gall_recommend::text').get()
            
            print('='*50)
            yield item
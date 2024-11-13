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
            for link in response.xpath('//tr[@itemscope][@itemtype="http://schema.org/Article"]'):
                # print(link)
                item = bobaeCommunityItem()
                
                item['gall_source']  = '수입차 커뮤니티'
                item['gall_title']   = link.css('.pl14 a::text').getall()[0]
                item['gall_url']     = link.css('a.bsubject::attr(href)').get()
                
                ##############################################################
                print('='*80)
                
                yield item
    
class commentCrawlSpider(scrapy.Spider):
    name = 'commentCrawl'
    comment_benz = []
    def start_requests(self):
        for i in range(1, 2, 1):
            yield scrapy.Request(
                f'https://www.bobaedream.co.kr/list?code=import&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={i}',
                callback=self.parse_comment,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
            )
            
    def parse_comment(self, response):
        for link in response.xpath('//tr[@itemscope][@itemtype="http://schema.org/Article"]'):
            item = bobaeCommunityItem()
            self.comment_benz.append(link.css('a.bsubject::attr(href)').get())
            gall_title = link.css('.pl14 a::text').getall()[0]
            item['gall_title']   = gall_title
            yield item
        print('='*80)
        
        for commentLink in self.comment_benz:
            full_url = 'https://www.bobaedream.co.kr' + commentLink
            yield scrapy.Request(full_url, callback=self.parse_takeComment, meta={'gall_title': gall_title})
        
    def parse_takeComment(self,response):
        item = bobaeCommunityItem()
        item['gall_title'] = response.meta.get('gall_title', 'NULL')
        item['gall_benz_comment'] = response.css('.commentlistbox dd::text').get()
        print('='*80)
        yield item
###################################################################################
class bobaeInfoSpider(scrapy.Spider):
    name = 'infoCrawl'
    
    def __init__(self, *args, **kwargs):
        super(bobaeInfoSpider, self).__init__(*args, **kwargs)
        self.comment_benz = []  # 댓글 링크들을 저장
        self.full_urls = []     # full_url들을 저장
        
    def start_requests(self):
        for i in range(2, 3, 1):
            yield scrapy.Request(
                f'https://www.bobaedream.co.kr/list?code=import&s_cate=&maker_no=&model_no=&or_gu=10&or_se=desc&s_selday=&pagescale=30&info3=&noticeShow=&s_select=&s_key=&level_no=&vdate=&type=list&page={i}',
                callback=self.parse_info,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
            )
    
    def parse_info(self, response):
        item = bobaeCommunityItem()
        for link in response.xpath('//tr[@itemscope][@itemtype="http://schema.org/Article"]'):
            self.comment_benz.append(link.css('a.bsubject::attr(href)').get())

            for commentLink in self.comment_benz:
                full_url = 'https://www.bobaedream.co.kr' + commentLink
                self.full_urls.append(full_url)
                item['gall_url'] = full_url
                yield scrapy.Request(full_url, callback=self.parse_takeComment)
        print(self.full_urls)

    def parse_takeComment(self, response):
        item = bobaeCommunityItem()
        item['gall_source']       = '외제차 게시판'
        item['gall_title'] = response.css('div.writerProfile strong::text').get()
        gall_content = response.css('div.bodyCont p::text').getall()
        newLst = []
        for it in gall_content:
            new = it.strip()
            if new :
                newLst.append(new)
        item['gall_content'] = newLst
        
        gall_benz_comment = response.css('div.commentlistbox dd::text').getall()
        newLst = []
        for it in gall_benz_comment:
            new = it.strip()
            if new :
                newLst.append(new)
        item['gall_benz_comment'] = newLst
        
        print('='*80)
        yield item
        
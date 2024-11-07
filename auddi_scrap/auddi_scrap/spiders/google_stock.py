import scrapy

class GoogleStockSpider(scrapy.Spider):
    name = "google_stock"
    allowed_domains = ['www.google.com']
    start_urls = ['https://www.google.com/finance/quote/005930:KRX?sa=X']

    def parse(self, response):
        stock_name  = response.css('div.zzDege::text').get()
        stock_price = response.css('div.YMlKec.fxKbKc::text').get()
        stock_date  = response.css('div.ygUjEc::text').get()
        stock_rise  = response.css('div.JwB6zf::text').get() 
        
        yield {
            'name'  : stock_name,
            'price' : stock_price,
            'date'  : stock_date,
            'rise'  : stock_rise
        }

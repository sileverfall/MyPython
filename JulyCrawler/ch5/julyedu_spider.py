import scrapy

class JulyeduSpider(scrapy.Spider):
    name = 'julyedu'
    start_urls = ['https://www.julyedu.com/category/index']
    
    def parse(self,response):
        for julyedu_class in response.xpath('//div[@class ="couse_info_box"]'):
            #//*[@id="main-container"]/div[2]/div[1]/div[3]
            #//*[@id="main-container"]/div[2]/div[1]/div[3]/a
            # //*[@id="main-container"]/div[2]/div[1]/div[3]
            print (julyedu_class.xpath('a/h4/text()')).extract_first()
            
            yield{'title':julyedu_class.xpath('a/h4/text()').extract_first()}
            
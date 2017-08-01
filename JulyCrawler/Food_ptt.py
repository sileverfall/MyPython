import scrapy

class FoodpttSpider(scrapy.Spider):
    name = 'Foodptt'
    start_urls = ['https://www.ptt.cc/bbs/Food/index.html']
    
    def parse(self,response):
        for Food_ptt in response.xpath('//div[@class ="r-ent"]'):
            #//*[@id="main-container"]/div[2]/div[1]/div[3]
            #//*[@id="main-container"]/div[2]/div[1]/div[3]/a
            # //*[@id="main-container"]/div[2]/div[1]/div[3]
            print (Food_ptt.xpath('div[@class ="title"]/text()')).extract()
            
            yield{'title':Food_ptt.xpath('div[@class ="title"]/text()').extract()}
            

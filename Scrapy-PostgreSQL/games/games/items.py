import scrapy


class GamesItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    url = scrapy.Field()
    alt_name = scrapy.Field()
    year = scrapy.Field()
    platform = scrapy.Field()
    released_in = scrapy.Field()
    genre = scrapy.Field()
    theme = scrapy.Field()
    publisher = scrapy.Field()
    developer = scrapy.Field()   
    perspectives = scrapy.Field()  

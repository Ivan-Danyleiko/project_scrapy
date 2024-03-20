import scrapy


class GetUrlsSpider(scrapy.Spider):
    name = "get_urls"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        pass

import scrapy


class GooglespiderSpider(scrapy.Spider):
    searchWord =""
    name = "googleSpider"
    allowed_domains = ["www.yahoo.co.jp"]
    start_urls = [f"https://www.yahoo.co.jp/search?q={searchWord}"]

    def parse(self, response):
        pass

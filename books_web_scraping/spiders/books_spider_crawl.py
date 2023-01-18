import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpiderCrawlSpider(CrawlSpider):
    name = 'books_spider_crawl'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r"/catalogue/[\w-]+/index\.html"), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r"page"), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        yield {'title': response.css('h1::text').get(),
               'price': response.css('.price_color::text').get(),
               'category': response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get(),
               'availability': response.xpath('//tr/th[contains(text(), "Availability")]/following-sibling::td/text()').get(),
               'product description': response.xpath('//div[contains(@id, "product_description")]/following-sibling::p/text()').get(),
               'image': response.urljoin(response.css('div.item > img::attr("src")').get())}
                

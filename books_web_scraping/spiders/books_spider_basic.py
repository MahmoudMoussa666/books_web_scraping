import scrapy
from scrapy.shell import inspect_response


class BooksSpiderBasic(scrapy.Spider):
    name = 'books_spider_basic'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.css('ol li article')

        for book in books:
            yield response.follow(book.css('h3 a::attr(href)').get(), callback=self.parse_book)

    def parse_book(self, response):
        yield {'title': response.css('h1::text').get(),
               'price': response.css('.price_color::text').get(),
               'category': response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get(),
               'availability': response.xpath('//tr/th[contains(text(), "Availability")]/following-sibling::td/text()').get(),
               'product description': response.xpath('//div[contains(@id, "product_description")]/following-sibling::p/text()').get(),
               'image': response.urljoin(response.css('div.item > img::attr("src")').get())}
                

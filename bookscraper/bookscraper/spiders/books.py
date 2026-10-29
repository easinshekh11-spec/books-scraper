import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        book =response.xpath('//ol[@class= "row"]/li/article')

        for book in book:
            Name = book.xpath('.//h3/a/@title').get()
            Price = book.xpath('.//div [@class="product_price"]/p/text()').get()
            rating = book.xpath('.//p/@class').get()
            stock = book.xpath('normalize-space(.//p[@class ="instock availability"])').get()
            product_url = book.xpath('.//div[@class = "image_container"]/a/@href').get()
           
                      
            yield {
                "title" : Name,
                "price": Price,
                "rating" : rating,
                "availability" : stock,
                "product_url" :response.urljoin(product_url),
            }
        next_page =response.xpath('.//li[@class="next"]/a/@href').get()

        if next_page:
            yield response.follow(next_page, callback = self.parse)

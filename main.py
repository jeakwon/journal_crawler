import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.nature.com/neuro/research',
    ]

    def parse(self, response):
        articles = response.xpath('//article')
        for article in articles:
            articletype = article.xpath('.//*[@data-test="article.type"]/text()').extract_first()
            datetime = article.xpath('.//*[@itemprop="datePublished"]/@datetime').extract_first()
            headline = article.xpath('.//*[@itemprop="name headline"]/a/text()').extract()
            headline = " ".join(headline)
            description = article.xpath('.//*[@itemprop="description"]//p/text()').extract()
            description = " ".join(description)

            if articletype.find('Correction') == -1:
                print('\n')
                print(articletype)
                print(datetime)
                print(headline)
                print(description)
                print('\n')

"""
Crawler for glance at journal.
Targe journal : Nature Neuroscience
Description : crawl every new articles updated in "last_friday" to "upcoming_thursday" (article except : "correction")
Format : Dictionary of {"ARTICLETYPE","DATETIME","HEADLINE","DESCRIPTION"} .csv file
"""

# Import Libraries
import scrapy
import datetime
from setdate import upcoming_weekday

datenow = datetime.datetime.now()
upcoming_thursday = upcoming_weekday(datenow, 4).date()
last_friday = upcoming_thursday - datetime.timedelta(7)

# Crawling Nature neuroscience reserch articles
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.nature.com/neuro/research',
    ]

    def parse(self, response):
        articles = response.xpath('//article')
        for article in articles:
            ARTICLETYPE = article.xpath('.//*[@data-test="article.type"]/text()').extract_first()
            if ARTICLETYPE.find('Correction') != -1:
                continue

            DATETIME = article.xpath('.//*[@itemprop="datePublished"]/@datetime').extract_first()
            DATE = datetime.datetime.strptime(DATETIME, '%Y-%m-%d').date()
            if not last_friday<DATE<upcoming_thursday:
                continue

            HEADLINE = article.xpath('.//*[@itemprop="name headline"]//text()').extract()
            HEADLINE = " ".join(HEADLINE)
            HEADLINE = HEADLINE.replace('\n','')
            HEADLINE = HEADLINE.replace('\t','')
            HEADLINE = HEADLINE.replace('  ','')

            DESCRIPTION = article.xpath('.//*[@itemprop="description"]//p/text()').extract()
            DESCRIPTION = " ".join(DESCRIPTION)

            yield {
            "Article" : ARTICLETYPE,
            "DATETIME" : DATETIME,
            "HEADLINE" : HEADLINE,
            "DESCRIPTION" : DESCRIPTION,
            }

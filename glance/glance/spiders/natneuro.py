# -*- coding: utf-8 -*-
import scrapy


class NatneuroSpider(scrapy.Spider):
    name = 'natneuro'
    allowed_domains = ['www.nature.com/neuro/research']
    start_urls = ['http://www.nature.com/neuro/research']

    def parse(self, response):
        articles = response.xpath('//article')
        for article in articles:
            ARTICLETYPE = article.xpath('.//*[@data-test="article.type"]/text()').extract_first()

            DATETIME = article.xpath('.//*[@itemprop="datePublished"]/@datetime').extract_first()

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

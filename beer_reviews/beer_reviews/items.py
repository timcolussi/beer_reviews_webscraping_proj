# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeerReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    aroma = scrapy.Field()
    appearance = scrapy.Field()
    flavor = scrapy.Field()
    mouthfeel = scrapy.Field()
    style = scrapy.Field()
    ABV = scrapy.Field()
    IBU = scrapy.Field()
    brewers_comments = scrapy.Field()
    panel_comments = scrapy.Field()
    editors_comments = scrapy.Field()
    


from beer_reviews.items import BeerReviewsItem
from scrapy import Spider, Request

class BeerReviewsSpider(Spider):
	name = 'beer_reviews_spider'
	allowed_ulrs = ['https://beerandbrewing.com']
	start_urls = ['https://beerandbrewing.com/beer-reviews/?q=&hPP=30&idx=cbb_web_review_search&p=0']

	def parse(self, response):
		pass

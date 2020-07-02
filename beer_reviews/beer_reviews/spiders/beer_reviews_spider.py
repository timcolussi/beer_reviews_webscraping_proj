from beer_reviews.items import BeerReviewsItem
from scrapy import Spider, Request

class BeerReviewsSpider(Spider):
	name = 'beer_reviews_spider'
	allowed_ulrs = ['https://beerandbrewing.com']
	start_urls = ['https://beerandbrewing.com/beer-reviews/?q=&hPP=30&idx=cbb_web_review_search&p=0']

	def parse(self, response):
		result_urls = [f'https://beerandbrewing.com/beer-reviews/?q=&hPP=30&idx=cbb_web_review_search&p={i}' for i in range(34)]

		for url in result_urls:
			yield Request(url=url, callback=self.parse_results_page)

	def parse_results_page(self, response):
		pass
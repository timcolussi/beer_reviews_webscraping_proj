from selenium import webdriver
import re
import time
import csv
import numpy as np
from selenium.webdriver.common.by import By

# set driver
driver = webdriver.Chrome(r'\Users\timco\Downloads\chromedriver_win32\chromedriver.exe')


# navigate to page
driver.get("https://beerandbrewing.com/beer-reviews/?q=&hPP=30&idx=cbb_web_review_search&p=0")

index = 1
hrefs = []
while index <=34:
#while index <=1:
	try:	
		# keep track where we are for debugging purposes
		print("Scraping Page number " + str(index))
		index = index + 1
		# making a list of links containing the info to scrape
		links = driver.find_elements_by_xpath('//div[@class="hit-content col-xs-12 col-sm-12 col-md-10 text-wrapper"]/a')
		for li in links:
			hrefs.append(li.get_attribute('href'))
		# insert a scroll
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		# locate and click the next button
		next_button = driver.find_element_by_xpath('//*[@id="pagination"]/div/ul/li[10]/a')
		next_button.click()
		time.sleep(2)
	except:
		break

# creating the output csv
csv_file = open('beer_reviews.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(['Name','Style','Brewer_comments','Panel_comments','Editor_comments','ABV','IBU','Score','Aroma','Appearance','Flavor','Mouthfeel'])
# iterating through list of links and scraping the data
index2 = 1
for href in hrefs:
	# keep track of where we are for debugging purposes
	print("Scraping beer number: " + str(index2))
	index2 = index2 + 1
	# creating an empty dictionary whose values will be written as lines in the output csv
	beers_dict = {}
	# using try/except to skip beers that have 'dead' website links
	try:
		driver.get(href)
		name = driver.find_element_by_xpath('//*[@id="article-body"]/h1').text
		style = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/p[1]').text
		try:
			brewer_comment = driver.find_element_by_xpath('//h4[contains(text(),"What the brewers say")]//following-sibling::p').text
		except:
			brewer_comment = np.nan
		try:
			panel_comment = driver.find_element_by_xpath('//h4[contains(text(),"What our panel thought")]//following-sibling::p').text
		except:
			panel_comment = np.nan
		try:
			editor_comment = driver.find_element_by_xpath('//h4[contains(text(),"What our editors thought")]//following-sibling::p').text
		except:
			editor_comment = np.nan
		# adding try/except in case ABV and IBU info is not available
		try:
			ABV = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/p[2]').text
			ABV = re.findall('\d*\.?\d+', ABV)[0]
		except:
			ABV = np.nan
		try:
			IBU = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/p[2]').text
			IBU = re.findall('\d*\.?\d+', IBU)[1]	 	
		except:
			IBU = np.nan
		score = driver.find_element_by_xpath('//div[@class="main-score-overall rating col-12"]').text
		score = re.findall('\d+', score)[0]
		aroma = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]').text
		appearance = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[2]').text
		flavor = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[2]').text
		mouthfeel = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[2]').text
		# adding values to the dictionary
		beers_dict['name'] = name
		beers_dict['style'] = style
		beers_dict['brewer_comments'] = brewer_comment
		beers_dict['panel_comments'] = panel_comment
		beers_dict['editor_comments'] = editor_comment
		beers_dict['ABV'] = ABV
		beers_dict['IBU'] = IBU
		beers_dict['score'] = score
		beers_dict['aroma']	= aroma
		beers_dict['appearance'] = appearance
		beers_dict['flavor'] = flavor
		beers_dict['mouthfeel'] = mouthfeel
		# writing the values to the output csv
		writer.writerow(beers_dict.values())
	except:
		pass	


csv_file.close()
driver.close()
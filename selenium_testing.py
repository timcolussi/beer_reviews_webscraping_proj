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

hrefs = []
links = driver.find_elements_by_xpath('//div[@class="hit-content col-xs-12 col-sm-12 col-md-10 text-wrapper"]/a')
for li in links:
	hrefs.append(li.get_attribute('href'))

csv_file = open('test2.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(['brewer_comments', 'panel_comments', 'editor_comments'])

for href in hrefs:
	comments_dict = {}
	driver.get(href)
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
	comments_dict['brewer_comments'] = brewer_comment
	comments_dict['panel_comments'] = panel_comment
	comments_dict['editor_comments'] = editor_comment
	writer.writerow(comments_dict.values())

csv_file.close()
driver.close()


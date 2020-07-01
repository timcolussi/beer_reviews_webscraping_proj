from selenium import webdriver
import re
import time
import csv

# set driver
driver = webdriver.Chrome(r'\Users\timco\Downloads\chromedriver_win32\chromedriver.exe')


# navigate to page
driver.get("https://beerandbrewing.com/beer-reviews/?q=&hPP=30&idx=cbb_web_review_search&p=0")

index = 1
hrefs = []
while index <=2:
	print("Scraping Page number " + str(index))
	index = index + 1
	links = driver.find_elements_by_xpath('//div[@class="hit-content col-xs-12 col-sm-12 col-md-10 text-wrapper"]/a')
	for li in links:
		hrefs.append(li.get_attribute('href'))
	# insert a scroll
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	# locate and click the next button
	next_button = driver.find_element_by_xpath('//*[@id="pagination"]/div/ul/li[10]/a')
	next_button.click()
	time.sleep(2)

csv_file = open('test.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
for href in hrefs:
	beers_dict = {}
	driver.get(href)
	name = driver.find_element_by_xpath('//*[@id="article-body"]/h1').text
	style = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/p[1]').text
	try:
	 	brewer_comments = driver.find_element_by_xpath('//*[@id="article-body"]/div[3]/p[1]').text
	except:
	 	brewer_comments = driver.find_element_by_xpath('//*[@id="article-body"]/div[2]/p[1]').text	 	
	try:
	 	panel_comments = driver.find_element_by_xpath('//*[@id="article-body"]/div[3]/p[2]').text	 
	except:
	 	panel_comments = driver.find_element_by_xpath('//*[@id="article-body"]/div[2]/p[2]').text	 	
	try:
	 	editor_comments = driver.find_element_by_xpath('//*[@id="article-body"]/div[3]/p[3]').text	 	
	except:
	 	editor_comments = driver.find_element_by_xpath('//*[@id="article-body"]/div[2]/p[3]').text	 	
	try:
		ABV = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/p[2]').text
		ABV = re.findall('\d*\.?\d+', ABV)[0]
	except:
		pass
	try:
	 	IBU = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/p[2]').text
	 	IBU = re.findall('\d*\.?\d+', IBU)[1]	 	
	except:
	 	pass
	score = driver.find_element_by_xpath('//div[@class="main-score-overall rating col-12"]').text
	score = re.findall('\d+', score)[0]
	aroma = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]').text
	appearance = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[2]').text
	flavor = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[2]').text
	mouthfeel = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[2]').text

	beers_dict['name'] = name
	beers_dict['style'] = style
	beers_dict['brewer_comments'] = brewer_comments
	beers_dict['panel_comments'] = panel_comments
	beers_dict['editor_comments'] = editor_comments
	beers_dict['ABV'] = ABV
	beers_dict['IBU'] = IBU
	beers_dict['score'] = score
	beers_dict['aroma']	= aroma
	beers_dict['appearance'] = appearance
	beers_dict['flavor'] = flavor
	beers_dict['mouthfeel'] = mouthfeel

	writer.writerow(beers_dict.values())	


#print(hrefs)
#print(len(hrefs))
# print(hrefs)
# print(len(hrefs))
# print(names)
# print(len(names))


driver.close()
from selenium import webdriver
import re


# set driver
driver = webdriver.Chrome(r'\Users\timco\Downloads\chromedriver_win32\chromedriver.exe')


# navigate to page
driver.get("https://beerandbrewing.com/beer-reviews/?q=&hPP=30&idx=cbb_web_review_search&p=0")

links = driver.find_elements_by_xpath('//div[@class="hit-content col-xs-12 col-sm-12 col-md-10 text-wrapper"]/a')
hrefs = []
for li in links:
	hrefs.append(li.get_attribute('href'))

mouthfeel_scores = []
for href in hrefs:
	driver.get(href)
	#name = driver.find_element_by_xpath('//*[@id="article-body"]/h1').text
	#style = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/p[1]').text
	# try:
	# 	b_comment = driver.find_element_by_xpath('//*[@id="article-body"]/div[3]/p[1]').text
	# 	brewer_comments.append(b_comment)
	# except:
	# 	b_comment = driver.find_element_by_xpath('//*[@id="article-body"]/div[2]/p[1]').text
	# 	brewer_comments.append(b_comment)
	# try:
	# 	p_comment = driver.find_element_by_xpath('//*[@id="article-body"]/div[3]/p[2]').text
	# 	panel_comments.append(p_comment)
	# except:
	# 	p_comment = driver.find_element_by_xpath('//*[@id="article-body"]/div[2]/p[2]').text
	# 	panel_comments.append(p_comment)
	# try:
	# 	e_comment = driver.find_element_by_xpath('//*[@id="article-body"]/div[3]/p[3]').text
	# 	editor_comments.append(e_comment)
	# except:
	# 	e_comment = driver.find_element_by_xpath('//*[@id="article-body"]/div[2]/p[3]').text
	# 	editor_comments.append(e_comment)
	# abv = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/p[2]').text
	# abv = re.findall('\d*\.?\d+', abv)[0]
	# try:
	# 	ibu = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/p[2]').text
	# 	ibu = re.findall('\d*\.?\d+', ibu)[1]
	# 	IBUs.append(ibu)
	# except:
	# 	pass
	# score = driver.find_element_by_xpath('//div[@class="main-score-overall rating col-12"]').text
	# score = re.findall('\d+', score)[0]
	#aroma = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]').text
	#appearance = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[2]').text
	#flavor = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[2]').text
	mouthfeel = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[2]').text
	mouthfeel_scores.append(mouthfeel)



#print(hrefs)
#print(len(hrefs))
print(mouthfeel_scores)
print(len(mouthfeel_scores))


driver.close()
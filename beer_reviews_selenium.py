from selenium import webdriver


# set driver
driver = webdriver.Chrome(r'\Users\timco\Downloads\chromedriver_win32\chromedriver.exe')

# navigate to page
driver.get("https://beerandbrewing.com/beer-reviews/?q=&hPP=30&idx=cbb_web_review_search&p=0")

links = driver.find_elements_by_xpath('//div[@class="hit-content col-xs-12 col-sm-12 col-md-10 text-wrapper"]/a')
link_list = []
for li in links:
	link_list.append(li.get_attribute('href'))

print(link_list)

driver.close()
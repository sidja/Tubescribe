from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL='http://128.199.167.207:9000/test_get_video'

def test_invalid_url(url):
	browser = webdriver.Firefox()
	browser.get(url)

	element = browser.find_element_by_id("main")
	print element.text
	print 
	#print element.get_attribute('value')
	assert 'youtube' in element.text

def fill_form(url):

	driver = webdriver.Firefox()
	#driver.set_window_size(1400,1000)
	#driver = webdriver.Firefox()
	driver.get(url)


	form = driver.find_element_by_id("youtubeUrl")
	#form.send_keys("some text")
	form.send_keys("https://www.youtube.com/watch?v=fakeed")

	driver.find_element_by_id("convertButton").click()

	
	try:
		element = WebDriverWait(driver, 10).until( 
		EC.presence_of_element_located((By.ID, "result3")) 
		)
		
	finally:
		driver.save_screenshot('out_phantom.png')
		driver.quit()



	#element = driver.find_element_by_id("result")




	# driver.save_screenshot('out.png')
	# driver.save_screenshot('screenie.png')
	
	# assert 'invalid' in element.text
	#driver.quit();

#test_invalid_url(URL)

fill_form(URL)
from selenium import webdriver
import unittest

class Check(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        
        URL='http://128.199.167.207:9000/test_get_video'

        self.browser.get(URL)

        
        #self.assertIn('To-Do', self.browser.title)  
        #self.fail('Finish the test!')  

        #driver = webdriver.Firefox()
        #driver.get(url)


        form = self.browser.find_element_by_id("youtubeUrl")
        #form.send_keys("some text")
        form.send_keys("https://www.youtube.com/watch?v=fakeed")

        self.browser.find_element_by_id("convertButton").click()
        

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
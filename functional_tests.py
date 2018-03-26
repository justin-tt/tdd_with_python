from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about an app. She goes online to check out 
        # its homepage
        self.browser.get('http://localhost:8000')
            
        # She notices the page title and header mention todo lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a todo item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        
        # She enters "Buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')
        
        # When she hits enter, the page updates, and now the page lists:
        # "1: Buy peacock feathers" as an item in the todo list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        
        # There is still a textbox waiting for her to enter another item.
        # She enters "Use peacock feathers to make a fly"
        self.fail('Finish the test!')
        
        # The page updates again, and now she has both items on her list
        
        # She wonders if the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is 
        # some explanatory note to that effect.
        
        # She visits that URL- her to-do list is still there
        
        # Satisfied, she goes back to sleep.
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')

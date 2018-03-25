from selenium import webdriver
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
        self.fail('Finish the test!')

        # She is invited to enter a todo item straight away
        
        # She enters "Buy peacock feathers"
        
        # When she hits enter, the page updates, and now the page lists:
        # "1: Buy peacock feathers" as an item in the todo list
        
        # There is still a textbox waiting for her to enter another item.
        # She enters "Use peacock feathers to make a fly"
        
        # The page updates again, and now she has both items on her list
        
        # She wonders if the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is 
        # some explanatory note to that effect.
        
        # She visits that URL- her to-do list is still there
        
        # Satisfied, she goes back to sleep.
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')

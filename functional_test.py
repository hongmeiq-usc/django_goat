from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	selenium_hub_url = 'http://192.168.59.103:4444/wd/hub' # this variable will be factored out in the future
	django_url = 'http://192.168.59.103:8000' # this variable will be factored out in the future

	def setUp(self):
		self.browser = webdriver.Remote(
			command_executor=self.selenium_hub_url,
			desired_capabilities={"browserName": "firefox"}) # open firefox browser on selenium hub
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()	
		
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to-do app. She goes
		# to check out its homepage
		self.browser.get(self.django_url) # go to django app url (assume django app is up)

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test')

		# She is invited to enter a to-do item straight away

		# She types "Buy peacock feathers" into a text box (Edith's hobby
		# is tying fly-fishing lures)

		# When she hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list

		# There is still a text box inviting her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)

		# The page updates again, and now shows both items on her list

		# Edith wonders whether the site will remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.

		# She visits that URL - her to-do list is still there.

		# Satisfied, she goes back to sleep


if __name__ == '__main__': 
	unittest.main(warnings='ignore')
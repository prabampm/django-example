#from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


# Create your tests here.
class AdminTest(LiveServerTestCase):
	fixtures = ['webapp/fixtures/admin.json']
	def setUp(self):
		self.browser = webdriver.Firefox()
	#def tearDown(self):
	#	self.browser.quit()
	def test_admin_site(self):
		# user opens web browser, navigates to admin page
		self.browser.get(self.live_server_url + '/admin/')
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)
		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('admin')
		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('admin')
		password_field.send_keys(Keys.RETURN)
		#login credentials are correct, and the user is ruser_link = self.browser.find_elements_by_link_text('Users')edirected to the main admin page
		user_link = self.browser.find_elements_by_link_text('Contacts')
		user_link[0].click()
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Select contact to change', body.text)
		user_link = self.browser.find_elements_by_link_text('Add contact')
		user_link[0].click()
		self.browser.find_element_by_name('first_name').send_keys("Praba")
		self.browser.find_element_by_name('last_name').send_keys("Karan")
		self.browser.find_element_by_name('email').send_keys("prabampm@gmail.com")
		# user clicks the save button
		self.browser.find_element_by_css_selector("input[value='Save']").click()
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('The contact "Praba Karan" was added successfully.', body.text)
		self.assertIn('Praba Karan', body.text)
		user_link = self.browser.find_elements_by_link_text('Praba Karan')
		user_link[0].click()
		
		






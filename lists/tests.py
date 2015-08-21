from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page # What function is that? It’s the view function we’re going to write next, which will actually return the HTML we want. You can see from the import that we’re planning to store it in lists/views.py. 


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # resolve is the function Django uses internally to resolve URLs, and find what view function they should map to. 
        self.assertEqual(found.func, home_page) # We’re checking that resolve, when called with “/”, the root of the site, finds a function called home_page. 
        
    def test_home_page_returns_correct_html(self):
    	request = HttpRequest() # We create an HttpRequest object, which is what Django will see when a user’s browser asks for a page. 
    	response = home_page(request) 
    	self.assertTrue(response.content.startswith(b'<html>'))
    	self.assertIn(b'<title>To-Do lists</title>', response.content)
    	self.assertTrue(response.content.endswith(b'</html>'))
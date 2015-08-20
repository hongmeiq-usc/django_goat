from selenium import webdriver

# browser = webdriver.Firefox()
# open firefox browser on selenium hub
selenium_hub_url = 'http://192.168.59.103:4444/wd/hub' # will be factored out
browser = webdriver.Remote(
	command_executor=selenium_hub_url,
	desired_capabilities={"browserName": "firefox"})

# go to django app url (assume django app is up)
django_url = 'http://192.168.59.103:8000' # will be factored out
browser.get(django_url)


assert 'Django' in browser.title

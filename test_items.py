import pytest
import time

def test_button_add_to_cart(browser):
	browser.implicitly_wait(10)
	browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
	elems = browser.find_elements_by_css_selector("button.btn-add-to-basket")
	assert len(elems) != 0, \
		"There are no button to cart on the page!"


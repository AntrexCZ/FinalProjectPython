import time

import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)  # Initialize Page Object, send url to constructor
        page.open()  # open the page
        page.go_to_login_page()  # execute method of the page, go to login page
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_be_empty_basket_message()

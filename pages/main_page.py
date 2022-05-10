from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

#    def go_to_login_page(self):
#        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#        link.click()
#        return LoginPage(browser=self.browser, url=self.browser.current_url)

#    def should_be_login_link(self):
#        self.browser.find_element(By.CSS_SELECTOR, "login_link_invalid"), "Login link is not present"
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_present_element(*BasketPageLocators.EMPTY_BASKET), "Item in basket"

    def should_be_empty_basket_message(self):
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty." in empty_message

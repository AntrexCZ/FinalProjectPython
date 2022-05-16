from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET)

    def should_be_winter_promo(self):
        # Check if the link is New Year promo
        assert "promo=newYear" in self.url, "This is not New Year's Promo"

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def should_be_success_message(self):
        assert "has been added to your basket." in self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)

    def should_be_book_price_same_as_basket_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_book_price = self.browser.find_element(*ProductPageLocators.BOOK_BASKET_PRICE).text
        assert book_price == basket_book_price, "The price of the books in not the same"

    def should_be_book_name_same_as_basket_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print("Book name : ...", book_name)
        book_basket_name = self.browser.find_element(*ProductPageLocators.BOOK_BASKET_NAME).text
        print("Basket : ... ", book_basket_name)
        assert book_name == book_basket_name, "The name of the books is different"

    def should_be_success_message(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert "has been added to your basket." in success_message, "Success message is not present"

    def should_not_be_success_message(self):
        assert self.is_not_present_element(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

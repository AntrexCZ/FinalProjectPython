from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.url, "This is not login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"

    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_address.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        password_field2.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button_submit.click()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Choose language: ru, en, ..(etc)")

# for Chrome
options = Options()
options.add_experimental_option('prefs', {'int.accept_languages': "language"})
# for Firefox
fp = webdriver.FirefoxProfile()
fp.set_preference("int_languages", "language")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    user_language = request.config.getoption("language")

    yield browser

    print("\nquit browser..")
    browser.quit()
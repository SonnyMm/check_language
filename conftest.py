import pytest
from selenium import webdriver

# Обработка аргумента командной строки --language
def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Choose language"
    )
# Фикстура browser, которая получает параметр language из командной строки
@pytest.fixture
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    browser = webdriver.Chrome(options=options)
    
    yield browser
    browser.quit()

# test_items.py
import time

def test_add_to_basket_button(browser):
    # Переход на страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Задержка для визуальной проверки текста кнопки

    # Поиск кнопки добавления в корзину
    add_to_basket_button = browser.find_element("css selector", ".btn-add-to-basket")

    # Проверка наличия кнопки
    assert add_to_basket_button, "Кнопка добавления в корзину не найдена"

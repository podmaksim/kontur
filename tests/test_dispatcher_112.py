from pages.main_page import MainPage
from pages.fire_page import FirePage
from pages.google_page import GooglePage
from time import sleep


def test_dispatcher(browser):
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.try_it_click_button()
    fire_page = FirePage(browser)
    fire_page.open_fire_page()
    fire_page.find_enter_element_field()
    fire_page.search_button_click()
    fire_page.targeted_address()
    fire_page.targeted_address_id()
    browser.get('https://www.google.by/maps/@53.706657,27.747712,7z?hl=ru')
    google_page = GooglePage(browser)
    google_page.enter_google()
    google_page.button_search_click()
    google_page.google_address()
    sleep(5)

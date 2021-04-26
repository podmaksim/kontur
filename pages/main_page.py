from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocator


class MainPage(BasePage):

    def try_it_click_button(self):
        try_it_button = self.find_element(
            MainPageLocator.LOCATOR_TRY_IT_BUTTON)
        try_it_button.click()

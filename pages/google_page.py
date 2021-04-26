from pages.fire_page import FirePage
from locators.google_page_locator import GooglePageLocator
import json


class GooglePage(FirePage):

    def enter_google(self):
        field = self.find_element(
            GooglePageLocator.LOCATOR_GOOGLE)
        with open('data.txt') as file:
            data = json.load(file)
            print(data['dolgota'], data['szirota'])
        field.send_keys(data['szirota'], ' ', data['dolgota'])

    def button_search_click(self):
        button_search = self.find_element(
            GooglePageLocator.LOCATOR_SEARCH_BUTTON)
        button_search.click()

    def google_address(self):
        google_street = self.find_element(
            GooglePageLocator.LOCATOR_GOOGLE_ADDRESS).text
        with open('data.txt') as file:
            data = json.load(file)
        # print(google_street[4:])
        # print(data['street'][6:])
        assert data['street'][6:] in google_street[4:]







from pages.main_page import MainPage
from locators.fire_page_locator import FirePageLocator
import json


class FirePage(MainPage):

    def open_fire_page(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def find_enter_element_field(self):
        element_field = self.find_element(
            FirePageLocator.LOCATOR_ENTER_ELEMENT_FIELD)
        element_field.click()
        element_field.send_keys('притыцкого 152')

    def search_button_click(self):
        search_button = self.find_element(
            FirePageLocator.LOCATOR_SEARCH_BUTTON)
        search_button.click()

    def targeted_address(self):
        address = self.find_element(
            FirePageLocator.LOCATOR_TARGETED_ADDRESS)
        address.click()

    def targeted_address_id(self):
        dolgota = ''
        szirota = ''
        address_street = ''
        address_id = self.find_element(
            FirePageLocator.LOCATOR_TARGETED_ADDRESS_ID).get_attribute("id")
        for i in address_id:
            if i != '|':
                dolgota = dolgota + i
                address_id = address_id[1:]
            else:
                szirota = address_id[1:]
                break
        address_street_1 = self.find_element(
            FirePageLocator.LOCATOR_ADDRESS).text

        for j in address_street_1:
            if j != ',':
                address_street = address_street + j

        data = {
            'dolgota': dolgota,
            'szirota': szirota,
            'street': address_street
        }

        with open('data.txt', 'w') as coordinates:
            json.dump(data, coordinates)




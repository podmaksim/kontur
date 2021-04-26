from selenium.webdriver.common.by import By


class FirePageLocator:
    LOCATOR_ENTER_ELEMENT_FIELD = (By.XPATH, '//input[@id="search-bar"]')
    LOCATOR_SEARCH_BUTTON = (By.XPATH, '//div[@class="Input_icons__3awLY"]//button[@class="SearchBar_icon__1AuUj"][1]')
    LOCATOR_TARGETED_ADDRESS = (By.XPATH, '//div[@class="DropDown_selectable__yz7nd"][1]')
    LOCATOR_TARGETED_ADDRESS_ID = (By.XPATH, '//div[@class="DropDown_selectable__yz7nd DropDown_selected__8vJmT"]//input[@class="DropDown_radio__2NqyD"]')
    LOCATOR_ADDRESS = (By.XPATH, '//div[@class="DropDown_selectable__yz7nd DropDown_selected__8vJmT"]//div[@class="component_address__n6AvQ"]')

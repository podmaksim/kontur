from selenium.webdriver.common.by import By


class GooglePageLocator:
    LOCATOR_GOOGLE = (By.XPATH, '//input[@id="searchboxinput"]')
    LOCATOR_SEARCH_BUTTON = (By.XPATH, '//button[@id="searchbox-searchbutton"]')
    LOCATOR_GOOGLE_ADDRESS = (By.XPATH, '//div[@class="section-info gm2-body-2 section-info-hoverable"][1]//span[@class="widget-pane-link"]')

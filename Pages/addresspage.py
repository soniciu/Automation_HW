import time
from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Pages.homepage import BasePage


class AddressPage(BasePage):

    def advance_order(self):
        try:
            checkout_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.address_proceed_to_checkout_button_xpath))
            )
            checkout_button_element.click()
        except:
            self.driver.quit()

    # TODO text verification method for order

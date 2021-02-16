import time
from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Pages.homepage import BasePage


class PaymentPage(BasePage):
    def confirm_order(self):
        try:
            payment_option_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.bank_wire_confirm_order_button_xpath))
            )
            payment_option_button_element.click()
        except:
            self.driver.quit()


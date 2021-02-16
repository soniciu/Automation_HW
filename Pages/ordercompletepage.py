import time
from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Pages.homepage import BasePage


class OrderCompletePage(BasePage):
    def complete_order(self):
        try:
            back_to_orders_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.back_to_orders_button_xpath))
            )
            back_to_orders_button.click()
        except:
            self.driver.quit()

    def get_amount_to_pay(self):
        try:
            amount = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.XPATH, Locators.summary_amount_to_pay_xpath))
            )
            return amount.text
        except:
            self.driver.quit()
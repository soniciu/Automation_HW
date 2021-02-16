from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):

    def add_first_item_to_cart(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_xpath(Locators.item_1_hover_xpath)) \
            .move_to_element(self.driver.find_element_by_xpath(Locators.item_1_add_to_cart_button_xpath)) \
            .click().perform()

    def add_second_item_to_cart(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_xpath(Locators.item_2_hover_xpath)) \
            .move_to_element(self.driver.find_element_by_xpath(Locators.item_2_add_to_cart_button_xpath)) \
            .click().perform()

    def add_third_item_to_cart(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_xpath(Locators.item_3_hover_xpath)) \
            .move_to_element(self.driver.find_element_by_xpath(Locators.item_3_add_to_cart_button_xpath)) \
            .click().perform()

    def continue_shopping(self):
        try:
            checkout_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.checkout_modal_cont_shopping_button_xpath))
            )
            checkout_button_element.click()
        except:
            self.driver.quit()

    def proceed_checkout(self):
        try:
            checkout_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.checkout_modal_proceed_button_xpath))
            )
            checkout_button_element.click()
        except:
            self.driver.quit()

    def sign_in(self):
        try:
            signin_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.homepage_sign_in_button_xpath))
            )
            signin_button_element.click()
        except:
            self.driver.quit()

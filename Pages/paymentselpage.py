from resources.lib import *


# Select payment page methods

class PaymentSelectionPage(BasePage):
    def advance_order_by_wire(self):
        try:
            payment_option_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.pay_by_wire_button_xpath))
            )
            payment_option_button_element.click()
        except:
            self.driver.quit()

    def advance_order_by_check(self):
        try:
            payment_option_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.pay_by_check_button_xpath))
            )
            payment_option_button_element.click()
        except:
            self.driver.quit()


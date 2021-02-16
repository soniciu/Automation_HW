from resources.lib import *


# Payment page methods

class PaymentPage(BasePage):
    def confirm_order(self):
        try:
            payment_option_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.bank_wire_confirm_order_button_xpath))
            )
            payment_option_button_element.click()
        except:
            self.driver.quit()


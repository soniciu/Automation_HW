from resources.lib import *


class ShippingPage(BasePage):
    def confirm_shipping(self):
        try:
            checkout_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.shipping_proceed_to_checkout_button_xpath))
            )
            self.driver.find_element_by_id(Locators.tos_checkbox_id).click()
            checkout_button_element.click()
        except:
            self.driver.quit()
from resources.lib import *


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

from resources.lib import *


# Order Summary page methods

class SummaryPage(BasePage):

    def proceed_to_checkout(self):
        try:
            checkout_button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.summary_checkout_button_xpath))
            )
            checkout_button_element.click()
        except:
            self.driver.quit()

    def get_payment_summary(self):
        try:
            to_pay = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.summary_amount_to_pay_xpath))
            )
            return to_pay.text
        except:
            self.driver.quit()

    def get_product_ids(self):
        prod_id_list = []
        item_list = self.driver.find_element_by_id('cart_summary'). \
            find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        for item in item_list:
            prod_id_list.append(item.get_attribute('id').split('product')[1])

        return prod_id_list

    def get_product_price(self, product_id):
        return float(self.driver.find_element_by_id(Locators.summary_price_id_prefix +
                                                    '_'.join(product_id.split('_')[0:4])).text.strip('$'))

    def get_total_product_price(self, product_id):
        return float(self.driver.find_element_by_id(Locators.summary_total_product_price_prefix +
                                                    '_'.join(product_id.split('_')[0:4])).text.strip('$'))

    def get_final_price(self):
        return float(self.driver.find_element_by_id(Locators.summary_total_price).text.strip('$'))

    def get_product_quantity(self, product_id):
        return float(self.driver.find_element_by_name(Locators.summary_quantity_id_prefix + product_id + '_hidden')
                     .get_attribute('value'))

    def increase_product_quantity(self, product_id, quantity):
        for i in range(quantity):
            try:
                increase = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, Locators.summary_increase_qty_btn_id_prefix + product_id))
                )
                increase.click()
                time.sleep(2)
            except:
                self.driver.quit()

    def decrease_product_quantity(self, product_id, quantity):
        if self.get_product_quantity(product_id) > quantity:
            for i in range(quantity):
                try:
                    decrease = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.ID, Locators.summary_decrease_qty_btn_id_prefix + product_id))
                    )
                    decrease.click()
                    time.sleep(2)
                except:
                    self.driver.quit()

    def remove_product(self, product_id):
        try:
            remove = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, product_id))
            )
            remove.click()
        except:
            self.driver.quit()

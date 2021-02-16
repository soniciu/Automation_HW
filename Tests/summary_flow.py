from resources.lib import *


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../resources/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # Add different products

    def test_add_products(self):
        self.driver.get("http://automationpractice.com/index.php")
        order = HomePage(self.driver)
        order.add_first_item_to_cart()
        time.sleep(2)
        order.continue_shopping()
        order.add_second_item_to_cart()
        time.sleep(2)
        order.continue_shopping()
        order.add_third_item_to_cart()
        order.proceed_checkout()

    # Manipulate quantities

    def test_quantities(self):
        cart = SummaryPage(self.driver)
        prod_item_id_list = cart.get_product_ids()
        inc_qty = 2
        dec_qty = 1
        for item in prod_item_id_list:
            start = cart.get_product_quantity(item)
            cart.increase_product_quantity(item, inc_qty)
            cart.decrease_product_quantity(item, dec_qty)
            final = cart.get_product_quantity(item)
            if final == start + inc_qty - dec_qty:
                print('SUCCESS')
            else:
                print('FAIL')

    def test_product_removal(self):
        cart = SummaryPage(self.driver)
        s_prod_item_id_list = cart.get_product_ids()
        item_no = len(s_prod_item_id_list)
        cart.remove_product(s_prod_item_id_list[0])
        if (item_no == len(cart.get_product_ids()) - 1) and (s_prod_item_id_list[0] not in cart.get_product_ids()):
            print('SUCCESS')
        else:
            print('FAIL')

    # Final order process

    def test_complete_order(self):
        login = LoginPage(self.driver)
        login.login_existing_user('abc@xyz.com', 'Test@123')

        address = AddressPage(self.driver)
        address.advance_order()

        ship = ShippingPage(self.driver)
        ship.confirm_shipping()

        pay_sel = PaymentSelectionPage(self.driver)
        pay_sel.advance_order_by_wire()

        pay = PaymentPage(self.driver)
        pay.confirm_order()

        done = OrderCompletePage(self.driver)
        done.complete_order()


    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")


if __name__ == '__main__':
    unittest.main()
from resources.lib import *


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../resources/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # Add products to cart form the homepage

    def test_add_product(self):
        self.driver.get("http://automationpractice.com/index.php")
        order = HomePage(self.driver)
        cart = SummaryPage(self.driver)
        order.add_first_item_to_cart()
        order.proceed_checkout()
        print(cart.get_payment_summary())
        cart.proceed_to_checkout()

    # Login existing user

    def test_login_user(self):
        login = LoginPage(self.driver)
        login.login_existing_user('abc@xyz.com', 'Test@123')  # The website prohibits automated logins

    # Complete the order process

    def test_confirm_address(self):
        address = AddressPage(self.driver)
        address.advance_order()

    def test_confirm_shipping(self):
        ship = ShippingPage(self.driver)
        ship.confirm_shipping()

    def test_select_pay_by_wire(self):
        pay_sel = PaymentSelectionPage(self.driver)
        pay_sel.advance_order_by_wire()

    def test_confirm_payment(self):
        pay = PaymentPage(self.driver)
        pay.confirm_order()

    def test_complete_order(self):
        done = OrderCompletePage(self.driver)
        done.complete_order()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()

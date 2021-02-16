from resources.lib import *


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../resources/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # Add product from the homepage

    def test_add_product(self):
        self.driver.get("http://automationpractice.com/index.php")
        order = HomePage(self.driver)
        cart = SummaryPage(self.driver)
        order.add_first_item_to_cart()
        order.proceed_checkout()
        print(cart.get_payment_summary())
        cart.proceed_to_checkout()

    # Start the new user creation process

    def test_create_new_user(self):
        login = LoginPage(self.driver)
        login.create_new_user('john@gmail.com')

    # Registration form filler, using given data. Can be replaced by DB queries

    def test_fill_registration_form(self):
        register = RegistrationPage(self.driver)
        user_data = Locators.user_data
        register.register_new_user(user_data)

    # Complete order process

    def test_confirm_address(self):
        address = AddressPage(self.driver)
        address.advance_order()
        time.sleep(10)

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

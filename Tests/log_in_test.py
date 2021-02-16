from resources.lib import *


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../resources/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # Testing the sign in functionality

    def test_sign_in_button(self):
        self.driver.get("http://automationpractice.com/index.php")
        order = HomePage(self.driver)
        order.sign_in()

    def test_enter_user_data(self):
        login = LoginPage(self.driver)
        login.login_existing_user('abc@xyz.com', 'Test@123') # The website prohibits automated logins
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")


if __name__ == '__main__':
    unittest.main()

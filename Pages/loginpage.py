from resources.lib import *


class LoginPage(BasePage):

    def login_existing_user(self, username, password):
        try:
            email_account_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, Locators.existing_email_texbox_id))
            )
            email_account_element.driver.find_element_by_id(Locators.existing_email_texbox_id).send_keys(str(username))
            time.sleep(2)
            self.driver.find_element_by_id(Locators.email_password_textbox_id).send_keys(str(password))
            time.sleep(2)
            self.driver.find_element_by_id(Locators.sign_in_button_id).click()
        except:
            self.driver.quit()

    def create_new_user(self, username):
        try:
            email_account_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, Locators.create_user_email_textbox_id))
            )
            email_account_element.click()
            email_account_element.send_keys(str(username))
            self.driver.find_element_by_id(Locators.create_user_button_id).click()
        except:
            self.driver.quit()

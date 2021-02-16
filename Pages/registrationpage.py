from resources.lib import *


class RegistrationPage(BasePage):
    def register_new_user(self, user_data):
        if (user_data.get('Radio Button') and
            user_data.get('Customer First Name') and
            user_data.get('Customer Last Name') and
            len(str(user_data.get('Customer Password'))) >= 5 and
            user_data.get('Address First Line') and
            user_data.get('Country') == 'United States' and
            user_data.get('Address City') and
            user_data.get('Address State') and
            len(str(user_data.get('Address Postcode'))) == 5 and
            str(user_data.get('Address Postcode')).isnumeric() and
            user_data.get('Mobile Phone Number') and
            str(user_data.get('Mobile Phone Number')).isnumeric() and
            user_data.get('Alias')
        ):
            try:
                gender_radio_button_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, Locators.gender_male_radio_button_id))
                )
                if user_data.get('Radio Button') == 'male':
                    gender_radio_button_element.click()
                else:
                    self.driver.find_element_by_id(Locators.gender_female_radio_button_id).click()

                self.driver.find_element_by_id(Locators.customer_first_name_textbox_id).send_keys(
                    str(user_data.get('Customer First Name')))

                self.driver.find_element_by_id(Locators.customer_last_name_textbox_id).send_keys(
                    str(user_data.get('Customer Last Name')))

                self.driver.find_element_by_id(Locators.user_password_textbox_id).send_keys(
                    str(user_data.get('Customer Password')))

                Select(self.driver.find_element_by_id(Locators.birthday_day_selector_id)).select_by_value(
                    str(user_data.get('Customer Birthday').split('/')[0]))

                Select(self.driver.find_element_by_id(Locators.birthday_month_selector_id)).select_by_value(
                    str(user_data.get('Customer Birthday').split('/')[1]))

                Select(self.driver.find_element_by_id(Locators.birthday_year_selector_id)).select_by_value(
                    str(user_data.get('Customer Birthday').split('/')[2]))

                if user_data.get('Newsletter') == 1:
                    self.driver.find_element_by_id(Locators.newsletter_checker_id).click()

                if user_data.get('Offers') == 1:
                    self.driver.find_element_by_id(Locators.offers_checker_id).click()

                self.driver.find_element_by_id(Locators.company_textbox_id).send_keys(
                    str(user_data.get('Company')))

                self.driver.find_element_by_id(Locators.address_line_one_textbox_id).send_keys(
                    str(user_data.get('Address First Line')))

                self.driver.find_element_by_id(Locators.address_line_two_textbox_id).send_keys(
                    str(user_data.get('Address Second Line')))

                self.driver.find_element_by_id(Locators.city_textbox_id).send_keys(
                    str(user_data.get('Address City')))

                Select(self.driver.find_element_by_id(Locators.country_selector_id)).select_by_value(
                    '21')  # Value of United States option in selector

                # TODO change so that value is found by state name
                Select(self.driver.find_element_by_id(Locators.state_selector_id)).select_by_value(
                    '32')  # Placeholder

                self.driver.find_element_by_id(Locators.postcode_textbox_id).send_keys(
                    str(user_data.get('Address Postcode')))

                self.driver.find_element_by_id(Locators.other_info_textbox_id).send_keys(
                    str(user_data.get('Other Info')))

                self.driver.find_element_by_id(Locators.phone_textbox_id).send_keys(
                    str(user_data.get('Regular Phone Number')))

                self.driver.find_element_by_id(Locators.mobile_phone_textbox_id).send_keys(
                    str(user_data.get('Mobile Phone Number')))

                self.driver.find_element_by_id(Locators.alias_textbox_id).clear()

                self.driver.find_element_by_id(Locators.alias_textbox_id).send_keys(
                    str(user_data.get('Alias')))

                # self.driver.find_element_by_id(Locators.submit_button_id).click()  # Register a new account
            except:
                self.driver.quit()


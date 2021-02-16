from resources.lib import *


class Locators():

    # Methods:

    def get_product_id(self):
        prod_id_list = []
        summary = SummaryPage(self.driver)
        item_list = self.driver.find_element_by_id('cart_summary').find_elements_by_css_selector("tr[id^='product']")
        for item in item_list:
            prod_id_list.append(item.get_attribute('id').split('product')[1])

        return prod_id_list

    # Test Data:

    user_data = {
        'Radio Button': 'Male',
        'Customer First Name': 'Terry',
        'Customer Last Name': 'Crews',
        'Customer Password': 'yogurt',
        'Customer Birthday': '30/7/1968',
        'Newsletter': 0,
        'Offers': 1,
        'Company': '99',
        'Address First Line': 'New York',
        'Address Second Line': 'Brooklyn',
        'Country': 'United States',
        'Address City': 'New York',
        'Address State': 'New York',
        'Address Postcode': '55443',
        'Other Info': 'Nope',
        'Regular Phone Number': '0123456768',
        'Mobile Phone Number': '0700123456',
        'Alias': 'The Falcon'
    }
    user_login_data = {'Username': 'abc@xyz.com', 'Password': 'Test@123'}

    # Home page locators:
        # Placeholder item locators
    item_1_hover_xpath = '//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]/img'
    item_1_add_to_cart_button_xpath = '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]/span'
    item_2_hover_xpath = '//*[@id="homefeatured"]/li[2]/div/div[1]/div/a[1]/img'
    item_2_add_to_cart_button_xpath = '//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a[1]/span'
    item_3_hover_xpath = '//*[@id="homefeatured"]/li[3]/div/div[1]/div/a[1]/img'
    item_3_add_to_cart_button_xpath = '//*[@id="homefeatured"]/li[3]/div/div[2]/div[2]/a[1]/span'
    item_4_hover_xpath = '//*[@id="homefeatured"]/li[4]/div/div[1]/div/a[1]/img'
    item_4_add_to_cart_button_xpath = '//*[@id="homefeatured"]/li[4]/div/div[2]/div[2]/a[1]/span'
    item_5_hover_xpath = '//*[@id="homefeatured"]/li[5]/div/div[1]/div/a[1]/img'
    item_5_add_to_cart_button_xpath = '//*[@id="homefeatured"]/li[5]/div/div[2]/div[2]/a[1]/span'
    item_6_hover_xpath = '//*[@id="homefeatured"]/li[6]/div/div[1]/div/a[1]/img'
    item_6_add_to_cart_button_xpath = '//*[@id="homefeatured"]/li[6]/div/div[2]/div[2]/a[1]/span'
    item_7_hover_xpath = '//*[@id="homefeatured"]/li[7]/div/div[1]/div/a[1]/img'
    item_7_add_to_cart_button_xpath = '//*[@id="homefeatured"]/li[7]/div/div[2]/div[2]/a[1]/span'

    checkout_modal_proceed_button_xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'
    checkout_modal_cont_shopping_button_xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span'
    checkout_modal_close_button_xpath = '//*[@id="layer_cart"]/div[1]/div[1]/span'
    homepage_sign_in_button_xpath = '//*[@id="header"]/div[2]/div/div/nav/div[1]/a'

    # Shopping cart summary, no login, page locators:

    summary_checkout_button_xpath = '//*[@id="center_column"]/p[2]/a[1]'
    summary_cont_shopping_button_xpath = '//*[@id="center_column"]/p[2]/a[2]'
    summary_amount_to_pay_xpath = '//*[@id="total_price"]'
    # Shopping cart, no login, item ID suffixes:
    #item_1_ID = '_1_1_0_0'
    #item_2_ID = '_2_7_0_0'
    #item_3_ID = '_5_19_0_0'
    #item_4_ID = '_3_13_0_0'
    #item_5_ID = '_4_16_0_0'
    #item_6_ID = '_6_31_0_0'
    #item_7_ID = '_7_34_0_0'
    # Shopping cart, no login, page locator ID prefixes:
    summary_total_product_price_prefix = 'total_product_price'
    summary_product_id_prefix = 'product'
    summary_price_id_prefix = 'product_price'
    summary_quantity_id_prefix = 'quantity'
    summary_decrease_qty_btn_id_prefix = 'cart_quantity_down'
    summary_increase_qty_btn_id_prefix = 'cart_quantity_up'
    summary_delete_id_prefix = ''
    summary_total_price = 'total_price'
    # TODO get locators for data checks within product descriptions

    '//*[@id="product_2_7_0_0"]'

    # Log in page locators:

    existing_email_texbox_id = 'email'
    email_password_textbox_id = 'passwd'
    sign_in_button_id = 'SubmitLogin'
    create_user_email_textbox_id = 'email_create'
    create_user_button_id = 'SubmitCreate'

    # Registration page locators:

    gender_male_radio_button_id = 'id_gender1'
    gender_female_radio_button_id = 'id_gender2'
    customer_first_name_textbox_id = 'customer_firstname'
    customer_last_name_textbox_id = 'customer_lastname'
    user_password_textbox_id = 'passwd'
    birthday_day_selector_id = 'days'
    birthday_month_selector_id = 'months'
    birthday_year_selector_id = 'years'
    newsletter_checker_id = 'newsletter'
    offers_checker_id = 'optin'
    company_textbox_id = 'company'
    address_line_one_textbox_id = 'address1'
    address_line_two_textbox_id = 'address2'
    city_textbox_id = 'city'
    state_selector_id = 'id_state'
    postcode_textbox_id = 'postcode'
    country_selector_id = 'id_country'
    other_info_textbox_id = 'other'
    phone_textbox_id = 'phone'
    mobile_phone_textbox_id = 'phone_mobile'
    alias_textbox_id = 'alias'
    submit_button_id = 'submitAccount'

    # Address page locators:

    address_selector_id = 'id_address_delivery'
    addresses_are_equal_checkbox_id = 'addressesAreEquals'
    delivery_address_update_button_xpath = '//*[@id="address_delivery"]/li[7]/a'
    billing_address_update_button_xpath = '//*[@id="address_invoice"]/li[7]/a'
    add_new_address_button_xpath = '//*[@id="center_column"]/form/div/p/a'
    order_comments_textarea_xpath = '//*[@id="ordermsg"]/textarea'
    address_proceed_to_checkout_button_xpath = '//*[@id="center_column"]/form/p/button'
    address_continue_shopping_button_xpath = '//*[@id="center_column"]/form/p/a'

    # Shipping page locators:

    tos_checkbox_id = 'cgv'
    tos_reader_xpath = '//*[@id="form"]/div/p[2]/a'
    tos_warning_window_close = '//*[@id="order"]/div[2]/div/div/a'
    shipping_proceed_to_checkout_button_xpath = '//*[@id="form"]/p/button'
    shipping_continue_shopping_button_xpath = '//*[@id="form"]/p/a'

    # Payment selection page locators:

    pay_by_wire_button_xpath = '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a'
    pay_by_check_button_xpath = '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a'
    payment_continue_shopping_button_xpath = '//*[@id="center_column"]/div/p/a'
    # TODO get locators for order checking against previous pages or specifications

    # Bank-wire payment page locators:

    bank_wire_other_payment_methods_xpath = '//*[@id="cart_navigation"]/a'
    bank_wire_confirm_order_button_xpath = '//*[@id="cart_navigation"]/button'
    # TODO get locators for data checks within confirmation box //*[@id="center_column"]/form/div

    # Check payment page locators:
    check_other_payment_methods_xpath = '//*[@id="cart_navigation"]/a'
    check_confirm_order_button_xpath = '//*[@id="cart_navigation"]/button'

    # Order completed page locators:

    back_to_orders_button_xpath = '//*[@id="center_column"]/p/a'
    cart_quantity_xpath = '//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[1]'
    amount_to_pay_xpath = '//*[@id="center_column"]/div/span/strong'
    amount_to_pay_2_xpath = '//*[@id="center_column"]/div/span'
    # TODO get locators for data checks within confirmation box //*[@id="center_column"]/div




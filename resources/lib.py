import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Pages.homepage import *
from Pages.summarypage import SummaryPage
from Pages.loginpage import LoginPage
from Pages.registrationpage import RegistrationPage
from Pages.addresspage import AddressPage
from Pages.shippingpage import ShippingPage
from Pages.paymentselpage import PaymentSelectionPage
from Pages.paymentpage import PaymentPage
from Pages.ordercompletepage import OrderCompletePage
from Locators.locators import Locators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helper import selenium_init, get_random_credential
from test import access_test, signup_wrong_password_test, signup_short_password_test, signup_wrong_email_test, signup_right_test, signin_test, user_profile_test

driver = selenium_init()

access_test(driver)

# credentials = get_random_credential()
# signup_test(driver, credentials)

credentials = dict(
	username='606project12',
	phone='97940156129',
    email='xuluming19189@gmail.com',
    wrong_email='yuchen.jiang011@outlook.com',
    password='xuluming1213',
    wrong_password='haonanya1',
    short_password='1234516'
)

signup_wrong_password_test(driver, credentials)

signup_short_password_test(driver, credentials)

signup_wrong_email_test(driver, credentials)

signup_right_test(driver, credentials)

signin_test(driver, credentials)

user_profile_test(driver)

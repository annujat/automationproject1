from selenium.webdriver.support.select import Select
from Library.ConfigParser import parse_details
from Pages.base import check_homepage_visibility

class Registration:
    def __init__(self, fixdriver):
        self.driver=fixdriver
        check_homepage_visibility(self.driver)

    def check_signin_visibility(self):
        self.driver.find_element("xpath", "//a[contains(text(),'/ Login')]").click()
        self.driver.find_element("xpath", "//h2[contains(text(),'New User')]").is_displayed()
        print("'New User Signup!' --is visible")

    def check_registration(self):
        self.driver.find_element("xpath", "//input[@data-qa='signup-name']").send_keys(parse_details("Details", "username"))
        self.driver.find_element("xpath", "//input[@data-qa='signup-email']").send_keys(parse_details("Details", "tempemail"))
        self.driver.find_element("xpath", "//button[text()='Signup']").click()
        self.driver.find_element("xpath", "//b[text()='Enter Account Information']").is_displayed()
        print("Enter Account Information -- is visible")

    def check_reg_with_used_email(self):
        self.driver.find_element("xpath", "//input[@data-qa='signup-name']").send_keys(parse_details("Details", "username2"))
        self.driver.find_element("xpath", "//input[@data-qa='signup-email']").send_keys(parse_details("Details", "email"))
        self.driver.find_element("xpath", "//button[text()='Signup']").click()
        self.driver.find_element("xpath", "//p[contains(text(),'Email Address')]").is_displayed()
        print("Email Address already exist  -- is visible")

    def fill_details(self):
        self.driver.find_element("id", "id_gender1").click()
        self.driver.find_element("id", "name").send_keys(parse_details("Details", "name"))
        self.driver.find_element("id", "email")
        self.driver.find_element("id", "password").send_keys(parse_details("Details", "password"))
        sel = Select(self.driver.find_element("id", "days"))
        sel.select_by_visible_text(parse_details("Details", "day"))
        sel = Select(self.driver.find_element("id", "months"))
        sel.select_by_index(parse_details("Details", "month"))
        sel = Select(self.driver.find_element("id", "years"))
        sel.select_by_value(parse_details("Details", "year"))
        self.driver.find_element("name", "newsletter").click()
        self.driver.find_element("name", "optin").click()

    def fill_address(self):
        self.driver.find_element("id", "first_name").send_keys(parse_details("Details", "firstname"))
        self.driver.find_element("id", "last_name").send_keys(parse_details("Details", "lastname"))
        self.driver.find_element("id", "company").send_keys(parse_details("Details", "company"))
        self.driver.find_element("xpath", "//input[@id='address1']").send_keys("Distt. Palwal,State Haryana")
        self.driver.find_element("xpath", "//input[@id='address2']").send_keys("Teh. Ballabhgarh,Distt Faridabad")
        sel = Select(self.driver.find_element("id", "country"))
        sel.select_by_index(0)
        self.driver.find_element("id", "state").send_keys(parse_details("Details", "state"))
        self.driver.find_element("id", "city").send_keys(parse_details("Details", "city"))
        self.driver.find_element("id", "zipcode").send_keys(parse_details("Details", "zipcode"))
        self.driver.find_element("id", "mobile_number").send_keys(parse_details("Details", "mobile"))

    def create_and_verify(self):
        self.driver.find_element("xpath", "//button[text()='Create Account']").click()
        self.driver.find_element("xpath", "//b[contains(text(),'Created!')]").is_displayed()
        print("ACCOUNT CREATED!-- is visible")
        self.driver.find_element("xpath", "//a[text()='Continue']").click()
        self.driver.find_element("xpath", "//a[contains(text(),'Logged in as')]").is_displayed()

    def delete_user(self):
        self.driver.find_element("xpath", "//a[contains(text(),'Delete Account')]").click()
        self.driver.find_element("xpath", "//b[contains(text(),'Deleted!')]").is_displayed()
        print("account deleted -- is visible")
        self.driver.find_element("xpath", "//a[text()='Continue']").click()




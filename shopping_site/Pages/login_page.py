from Pages.base import check_homepage_visibility
from Library.ConfigParser import parse_details


class Login:
    def __init__(self,fixdriver):
        self.driver=fixdriver
        check_homepage_visibility(self.driver)

    def check_login_visibility(self):
        self.driver.find_element("xpath", "//a[contains(text(),'/ Login')]").click()
        self.driver.find_element("xpath", "//h2[contains(text(),'Login to your')]").is_displayed()
        print("Login to your account-- is displayed")

    def check_login_with_correct(self):
        self.driver.find_element("xpath", "//input[@data-qa='login-email']").send_keys(parse_details("Details", "email"))
        self.driver.find_element("xpath", "//input[@data-qa='login-password']").send_keys(
            parse_details("Details", "password"))
        self.driver.find_element("xpath", "//button[@data-qa='login-button']").click()
        self.driver.find_element("xpath", "//a[contains(text(),'Logged in as')]").is_displayed()
        print("Logged in as user -- is displayed")

    def check_login_with_incorrect(self, data):
        self.driver.find_element("xpath", "//input[@data-qa='login-email']").send_keys(data[0])
        self.driver.find_element("xpath", "//input[@data-qa='login-password']").send_keys(data[1])
        self.driver.find_element("xpath", "//button[@data-qa='login-button']").click()
        self.driver.find_element("xpath", "//p[contains(text(),'password is incorrect!')]").is_displayed()
        print("Your email or password is incorrect! -- is displayed")

    def logout(self):
        self.driver.find_element("xpath", "//body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]").click()
        self.driver.get_screenshot_as_file("..\\Assets\\logout_error.png")
        if self.driver.find_element("xpath", "//h2[contains(text(),'Login to your')]").is_displayed():
            print("Login page-- is displayed")
        else:
            self.driver.get_screenshot_as_file("..\\Assets\\logout_error.png")

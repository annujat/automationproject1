from Pages.base import check_homepage_visibility
from Library.ConfigParser import parse_details
from selenium.webdriver.common.alert import Alert
from Library.text_generator import text_data



class ContactUs:
    def __init__(self,fixdrv):
        self.driver=fixdrv
        check_homepage_visibility(self.driver)

    def check_get_in_touch_visibility(self):
        self.driver.find_element("xpath", "//a[text()=' Contact us']").click()
        self.driver.find_element("xpath", "//h2[text()='Get In Touch']").is_displayed()
        print("get in touch ---is displayed")

    def fill_contact_form(self):
        self.driver.find_element("name", "name").send_keys(parse_details("Details", "username"))
        self.driver.find_element("name", "email").send_keys(parse_details("Details", "email"))
        self.driver.find_element("name", "subject").send_keys(text_data("subject"))
        self.driver.switch_to.alert.dismiss()
        self.driver.find_element("xpath",
                            "//body[1]/div[1]/div[2]/div[1]/div[1]/div[3]/form[1]/div[4]/textarea[1]").send_keys(
            text_data("message"))
        self.driver.find_element("name", "upload_file").send_keys(
            r"C:\Users\Aniket\PycharmProjects\shopping_site\Assets\logout_error.png")
        self.driver.find_element("name", "submit").click()
        alert = Alert(self.driver)
        alert.accept()
        self.driver.find_element("xpath", "//div[contains(text(),'Success!')]").is_displayed()
        print("Success! Your details have been submitted successfully ---is visible")

    def check_homepage_is_visible(self):
        self.driver.find_element("xpath", "//span[contains(text(),'Home')]").click()
        check_homepage_visibility(self.driver)

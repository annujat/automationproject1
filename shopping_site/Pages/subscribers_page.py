from Pages.base import check_homepage_visibility
from Library.ConfigParser import parse_details


class subscribe:
    def __init__(self,fixdrv):
        self.driver=fixdrv
        check_homepage_visibility(self.driver)

    def check_subscribe(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        self.driver.find_element("xpath", "//h2[text()='Subscription']").is_displayed()
        self.driver.find_element("id", "susbscribe_email").send_keys(parse_details("Details", "email"))
        self.driver.find_element("id", "subscribe").click()
        self.driver.find_element("xpath", "//div[@class='alert-success alert']").is_displayed()
        print("You have been successfully subscribed!' is visible")

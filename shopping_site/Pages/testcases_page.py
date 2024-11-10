from Pages.base import check_homepage_visibility


class test_cases:
    def __init__(self, fixdrv):
        self.driver = fixdrv
        check_homepage_visibility(self.driver)

    def check_testcases_page_visibility(self):
        self.driver.find_element("xpath", "//a[contains(text(),'Test Cases')]").click()
        self.driver.find_element("xpath", "//u[text()='Test Case 1: Register User']").is_displayed()
        print("testcases page is navigated successfully")

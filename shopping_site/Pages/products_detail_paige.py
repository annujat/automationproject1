from Pages.base import check_homepage_visibility
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class product_detail_page:
    def __init__(self,fixdrv):
        self.driver=fixdrv
        check_homepage_visibility(self.driver)

    def navigation_to_all_products(self):
        self.driver.execute_script("window.scrollTo(0,400);")
        self.driver.find_element("xpath", "//a[contains(text(),'Products')]").click()
        self.driver.find_element("xpath", "//h2[text()='All Products']").is_displayed()
        print("navigated to ALL PRODUCTS page successfully...")

    def product_detail_page(self):
        self.driver.find_element("xpath", "//a[text()='View Product']").click()
        self.driver.find_element("xpath",
                            "//body[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/h2[1]").is_displayed()
        print("name displayed")
        self.driver.find_element("xpath", "//span[contains(text(),'Rs.')]").is_displayed()
        print("name displayed")
        self.driver.find_element("xpath", "//p[contains(text(),'Category:')]").is_displayed()
        print("category displayed")
        self.driver.find_element("xpath", "//b[contains(text(),'Availability:')]").is_displayed()
        print("Availability displayed")
        self.driver.find_element("xpath", "//b[contains(text(),'Condition:')]").is_displayed()
        print("condition displayed")
        self.driver.find_element("xpath", "//b[contains(text(),'Brand:')]").is_displayed()
        print("brand displayed")

    def search_product(self):
        self.driver.execute_script("window.scrollTo(0,400);")
        self.driver.find_element("id", "search_product").send_keys("tshirt")
        self.driver.find_element("id", "submit_search").click()
        self.driver.execute_script("window.scrollTo(0,600);")
        self.driver.find_element("xpath", "//h2[contains(text(),'Searched Products')]").is_displayed()
        print("Searched Products -- is displayed")
        wait = WebDriverWait(driver=self.driver, timeout=10)
        wait.until(expected_conditions.visibility_of_element_located(
            ("xpath", "//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[7]/div[1]/div[2]/ul[1]/li[1]/a[1]")))
        print("all products are seen..")

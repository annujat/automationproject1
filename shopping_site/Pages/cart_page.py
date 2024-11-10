import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Pages.base import check_homepage_visibility


class add_to_cart:
    def __init__(self,driver):
        self.driver=driver
        check_homepage_visibility(self.driver)

    def check_add_to_cart(self):
        act = ActionChains(self.driver)
        act.click(self.driver.find_element("xpath", "//a[contains(text(),'Products')]")).perform()
        act.move_to_element(self.driver.find_element("xpath", "//a[@data-product-id='1']")).perform()
        act.click().perform()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of(
            self.driver.find_element("xpath", "//button[contains(text(),'Continue Shopping')]")))
        self.driver.find_element("xpath", "//button[contains(text(),'Continue Shopping')]").click()
        act.move_to_element(self.driver.find_element("xpath", "//a[@data-product-id='2']")).perform()
        act.click().perform()
        wait.until(expected_conditions.visibility_of(self.driver.find_element("xpath", "//u[contains(text(),'View Cart')]")))
        act.click(self.driver.find_element("xpath", "//u[contains(text(),'View Cart')]")).perform()
        time.sleep(3)

    def verify_cart_products(self):
        self.driver.find_element("xpath", "//a[contains(text(),'Blue Top')]").is_displayed()
        print("first item is displayed---")
        self.driver.find_element("xpath", "//a[contains(text(),'Men Tshirt')]").is_displayed()
        print("second item is displayed---")
        self.driver.find_element("xpath", "//tr[@id='product-1']/td[3]/p[1]").is_displayed()
        print("price is displayed---")
        self.driver.find_element("xpath", "//tr[@id='product-1']/td[4]/button").is_displayed()
        print("quantity is displayed")
        self.driver.find_element("xpath", "//tr[@id='product-1']/td[5]/p[1]").is_displayed()
        print("final price is displayed")


class product_quantity:
    def __init__(self,driver):
        self.driver=driver
        check_homepage_visibility(self.driver)

    def check_view_product(self):
        self.driver.find_element("xpath",
                            "//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element("xpath", "//b[text()='Availability:']").is_displayed()
        quantity = self.driver.find_element("id", "quantity")
        quantity.clear()
        quantity.send_keys("4")
        self.driver.find_element("xpath", "//button[@class='btn btn-default cart']").click()
        wait=WebDriverWait(self.driver,timeout=10)
        view_cart=wait.until(expected_conditions.visibility_of_element_located(("xpath","//u[text()='View Cart']")))
        view_cart.click()

    def check_in_cart(self):
        self.driver.find_element("xpath", "//a[text()='Sleeveless Dress']").is_displayed()
        quantity = self.driver.find_element("xpath", "//tr[@id='product-3']/td[4]/button")
        print(quantity.text)
        assert quantity.text == "4"
        print("exact quantity is displayed")

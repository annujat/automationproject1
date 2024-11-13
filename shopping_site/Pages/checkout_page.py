import time
from Library.text_generator import text_data
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Library.ConfigParser import parse_details
from Library.ConfigParser import parse_payment_card
from Pages.base import check_homepage_visibility

class Checkout:
    def __init__(self,fixdriver):
        self.driver = fixdriver
        check_homepage_visibility(self.driver)

    def check_logging_in(self):
        self.driver.find_element("xpath", "//a[contains(text(),'/ Login')]").click()
        self.driver.find_element("xpath", "//h2[contains(text(),'Login to your')]").is_displayed()
        self.driver.find_element("xpath", "//input[@data-qa='login-email']").send_keys(parse_details("Details", "email"))
        self.driver.find_element("xpath", "//input[@data-qa='login-password']").send_keys(
            parse_details("Details", "password"))
        self.driver.find_element("xpath", "//button[@data-qa='login-button']").click()
        logi=self.driver.find_element("xpath", "//a[contains(text(),'Logged in as')]")
        wait=WebDriverWait(driver=self.driver,timeout=10)
        wait.until(expected_conditions.visibility_of(logi))
        logi.is_displayed()
        print("Logged in as user -- is displayed")

    def check_add_to_cart(self):
        act = ActionChains(self.driver)
        act.click(self.driver.find_element("xpath", "//a[contains(text(),'Products')]")).perform()
        print("clicked on prioducts")
        act.scroll_by_amount(0,200).perform()
        time.sleep(3)
        print("scrolled successfully")
        act.move_to_element(self.driver.find_element("xpath", "//a[@data-product-id='1']")).perform()
        print("moved to element 1")
        act.click().perform()
        print("clicked on element 1")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of(
            self.driver.find_element("xpath", "//button[contains(text(),'Continue Shopping')]")))
        time.sleep(1)
        self.driver.find_element("xpath", "//button[contains(text(),'Continue Shopping')]").click()
        print("clicked on continue shopping")
        act.move_to_element(self.driver.find_element("xpath", "//a[@data-product-id='2']")).perform()
        act.click().perform()
        print("clicked on product 2")

    def check_cart(self):
        self.driver.find_element("xpath","//a[@href='/view_cart']").click()
        print("finally i'm in cart")
        self.driver.find_element("xpath","//li[contains(text(),'Shopping Cart')]").is_displayed()
        print("cart is displayed")

    def check_checkout(self):
        self.driver.find_element("xpath","//a[text()='Proceed To Checkout']").click()
        print("opened checkout page")
        self.driver.execute_script("window.scrollTo(0,100);")
        time.sleep(3)
        print("verified details")
        self.driver.execute_script("window.scrollTo(0,100);")
        time.sleep(3)
        print("reviewed order")
        self.driver.find_element("xpath", "//textarea[@name='message']").send_keys(text_data("checkout"))
        print("filled description")
        self.driver.find_element("xpath", "//a[text()='Place Order']").click()
        self.driver.find_element("xpath", "//li[text()='Payment']").is_displayed()

    def fill_payment_details(self):
        self.driver.find_element("name","name_on_card").send_keys(parse_payment_card("Card","name"))
        self.driver.find_element("name", "card_number").send_keys(parse_payment_card("Card", "number"))
        self.driver.find_element("name", "cvc").send_keys(parse_payment_card("Card", "cvc"))
        self.driver.find_element("name", "expiry_month").send_keys(parse_payment_card("Card", "exp_month"))
        self.driver.find_element("name", "expiry_year").send_keys(parse_payment_card("Card", "exp_year"))
        print("filled all details")

    def place_order(self):
        self.driver.find_element("id","submit").click()
        ele=self.driver.find_element("xpath", "//b[text()='Order Placed!']")
        wait=WebDriverWait(self.driver,timeout=10)
        wait.until(expected_conditions.visibility_of(ele)).is_displayed()
        print("order placed successfully")
        self.driver.find_element("xpath", "//a[text()='Continue']").click()



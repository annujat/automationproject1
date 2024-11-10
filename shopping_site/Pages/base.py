from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def check_homepage_visibility(driver):
    driver.execute_script("window.scrollBy(0,200);")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_element_located(("xpath", "//h2[text()='Category']")))
    print("homepage is visible")
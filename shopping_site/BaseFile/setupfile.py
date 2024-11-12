import pytest
from selenium import webdriver
from Library import ConfigParser


@pytest.fixture(scope="function")
def setup(request):
    global driver
    browser = ConfigParser.parse_driver("Name", "chromedriver")
    if browser == "chrome":
        ser = webdriver.ChromeService(executable_path=ConfigParser.parse_driver("Drivers", "chrome"))
        opt = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=ser, options=opt)
    elif browser == "firefox":
        ser = webdriver.FirefoxService(executable_path=ConfigParser.parse_driver("Drivers", "firefox"))
        opt = webdriver.FirefoxOptions()
        opt.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        driver = webdriver.Firefox(options=opt, service=ser)

    driver.get(ConfigParser.parse_driver("Websites", "automation_exercise"))
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.quit()

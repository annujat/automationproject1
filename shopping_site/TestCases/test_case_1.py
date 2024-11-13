import pytest
from Library.DataGenerator import generate_data
import Pages
from BaseFile.setupfile import setup


@pytest.mark.account
@pytest.mark.usefixtures("setup")
class Test_Registration:
    def test_signin_1(self):
        reg = Pages.registration_page.Registration(self.driver)
        reg.check_signin_visibility()
        reg.check_registration()
        reg.fill_details()
        reg.fill_address()
        reg.create_and_verify()
        reg.delete_user()

    def test_register_used_email_5(self):
        usd = Pages.registration_page.Registration(self.driver)
        usd.check_signin_visibility()
        usd.check_reg_with_used_email()


@pytest.mark.account
@pytest.mark.usefixtures("setup")
class Test_LoginPage:
    def test_login_correct_2(self):
        logi = Pages.login_page.Login(self.driver)
        logi.check_login_visibility()
        logi.check_login_with_correct()

    @pytest.mark.parametrize("data", generate_data())
    def test_login_incorrect_3(self, data):
        logi = Pages.login_page.Login(self.driver)
        logi.check_login_visibility()
        logi.check_login_with_incorrect(data)

    def test_logout_user_4(self):
        lgn = Pages.login_page.Login(self.driver)
        lgn.check_login_visibility()
        lgn.check_login_with_correct()
        lgn.logout()


@pytest.mark.query
@pytest.mark.usefixtures("setup")
class Test_ContactUs_page:
    def test_contact_us_form_6(self):
        con = Pages.contact_page.ContactUs(self.driver)
        con.check_get_in_touch_visibility()
        con.fill_contact_form()
        con.check_homepage_is_visible()


@pytest.mark.visibility
@pytest.mark.usefixtures("setup")
class Test_TestCases_page:
    def test_test_cases_7(self):
        tes = Pages.testcases_page.test_cases(self.driver)
        tes.check_testcases_page_visibility()


@pytest.mark.visibility
@pytest.mark.usefixtures("setup")
class Test_Products_Page:
    def test_product_detail_page_8(self):
        pro = Pages.products_detail_paige.product_detail_page(self.driver)
        pro.navigation_to_all_products()
        pro.product_detail_page()

    def test_product_search_9(self):
        sea = Pages.products_detail_paige.product_detail_page(self.driver)
        sea.navigation_to_all_products()
        sea.search_product()


@pytest.mark.visibility
@pytest.mark.usefixtures("setup")
class Test_Subscription:
    def test_subscribe_10(self):
        sub = Pages.subscribers_page.subscribe(self.driver)
        sub.check_subscribe()


@pytest.mark.cart
@pytest.mark.usefixtures("setup")
class Test_cart:

    def test_add_to_cart(self):
        ad = Pages.cart_page.add_to_cart(self.driver)
        ad.check_add_to_cart()
        ad.verify_cart_products()

    def test_product_quantity(self):
        qua = Pages.cart_page.product_quantity(self.driver)
        qua.check_view_product()
        qua.check_in_cart()


@pytest.mark.order
@pytest.mark.usefixtures("setup")
class Test_checkout:

    def test_login(self):
        lg = Pages.checkout_page.Checkout(self.driver)
        lg.check_logging_in()
        lg.check_add_to_cart()
        lg.check_cart()
        lg.check_checkout()
        lg.fill_payment_details()
        lg.place_order()

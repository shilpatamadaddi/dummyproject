import pytest

from base.login_page import Login_page


class Test_01_Admin_Login:

    admin_page_url = "https://www.flipkart.com/"
    username = "shilpa.tamadaddiemail@gmail.com"

    def test_title_verification(self, driver):

        driver.get(self.admin_page_url)

        act_title = driver.title
        print("Actual title:", act_title)
        exp_title = "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!'"

        if act_title != exp_title:
            driver.save_screenshot("screenshots/homepage_failed.png")

        assert act_title == exp_title

    @pytest.mark.regression
    def test_valid_admin_login(self, driver):

        driver.get(self.admin_page_url)

        self.log = Login_page(driver)

        self.log.enter_login()
        self.log.enter_email()
        self.log.enter_username(self.username)
        self.log.login_button2()

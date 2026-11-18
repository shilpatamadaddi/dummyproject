
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page:

    user_login_xpath = "//span[text()='Login']"
    user_email_click = "//span[text()='Use Email-ID']"
    user_login = "//input[@type='email']"
    login_button = "//button[text()='Continue']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_login(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.user_login_xpath)
            )
        ).click()

    def enter_email(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.user_email_click)
            )
        ).click()

    def enter_username(self, email):
        email_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.user_login)
            )
        )
        email_field.clear()
        email_field.send_keys(email)

    def login_button2(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, self.login_button)
            )
        ).click()

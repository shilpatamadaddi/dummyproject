from playwright.sync_api import Page
import time


def test_setup(page: Page):
    page.goto("https://www.flipkart.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    print("Page title:", page.title())

    time.sleep(5)


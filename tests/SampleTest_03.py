from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage


class TestLogin():

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(
            executable_path="C:/Users/secse6/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe")
        driver.delete_all_cookies()
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

    def test_logout(self, test_setup):
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

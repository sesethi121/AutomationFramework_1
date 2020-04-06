from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
fs
class TestLogin():

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/secse6/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_login(self, test_setup):
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

        #driver.find_element_by_id("txtUsername").send_keys("Admin")
        #driver.find_element_by_id("txtPassword").send_keys("admin123")
        #driver.find_element_by_id("btnLogin").click()

    def test_logout(self, test_setup):
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        #driver.find_element_by_id("welcome").click()
        #driver.find_element_by_link_text("Logout").click()

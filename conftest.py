import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type the browser name i.e chrome or firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Users/secse6/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:/Users/secse6/PycharmProjects/AutomationFramework_1/drivers/geckodriver.exe")

    elif browser == 'ie':
        driver = webdriver.ie(executable_path="C:/Users/secse6/PycharmProjects/AutomationFramework_1/drivers/IEDriverServer.exe")

    driver.delete_all_cookies()
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # Tear down information
    driver.close()
    driver.quit()
    print("Test completed")
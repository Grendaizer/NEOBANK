import pytest
from selenium import webdriver


@pytest.fixture(scope='function', autouse=False)
def initdriver():
    driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(time_to_wait=10)
    driver.set_window_size(1024, 600)
    yield driver
    driver.quit()


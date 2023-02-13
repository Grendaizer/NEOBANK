import time

from selenium.webdriver.common.by import By


class Home_Page:
    INPUTNUMBER = '/html/body/app-root/auth-page/div[2]/bpm-auth-login/form/md-form-field/div/div[2]/input'
    BUTTON = '#btnNext'
    TEXT = '#formAuthQr > div.auth-form-title'

    def __init__(self, driver):
        self.driver = driver

    def opentab(self):
        self.driver.get('https://web.neobank.one/auth/login')

    def check_titlename(self, name: str):
        title = self.driver.title
        assert name == title

    def enter_number(self, number: str):
        time.sleep(5)
        replaced = number.replace('+380', '')
        numinput = self.driver.find_element(By.XPATH, self.INPUTNUMBER)
        numinput.send_keys(replaced)

    def click_button_continue(self):
        button = self.driver.find_element(By.CSS_SELECTOR, self.BUTTON)
        button.click()
        time.sleep(5)

    def enable_fullscreen_mode(self):
        self.driver.maximize_window()
        time.sleep(1)

    def check_text_on_page(self, checked_text):
        time.sleep(1)
        source_text = self.driver.find_element(By.CSS_SELECTOR, self.TEXT)
        assert source_text.text == checked_text

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class AutomateForm:

    def __init__(self, PATH, url, headless=False):

        chrome_options = Options()

        if headless:
            chrome_options.set_headless()

        self.driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
        self.driver.get(url)
        self.name_field = None

        time.sleep(300)

    def find_and_set_field(self, name, value, alt_name):

        present = False
     
        # find field by name, label, placeholder
        try:
            self.findByName(name)
            present = True
        except Exception as e:
            print(e)

    def findByName(self, name):
        self.name_field = self.driver.find_element(by=By.NAME, value=name)

    def findById(self, name):
        self.name_field = self.driver.find_element(by=By.ID, value=name)

    def searchByPlaceholder(self, name):
        place_holder_xpath = f"//input[@placeholder={name}]"
        self.name_field = self.driver.find_element(by=By.XPATH, place_holder_xpath)

    def findByLabel(self, name):
        self.name_field = self.driver.find_element(by=By.ID, value=name)

    def submit_btn(self):

        button = self.driver.find_element(by=By.XPATH, "//input[@type='submit']")
        button.click()

        # print(form.text)
        # name.send_keys(first_name)
        # name.send_keys(Keys.RETURN)
        # driver.implicitly_wait(5)
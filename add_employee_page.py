from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def enter_first_name(self, first_name):
        self.wait.until(EC.presence_of_element_located(
            (By.NAME, "firstName"))).send_keys(first_name)
    
    def enter_last_name(self, last_name):
        self.wait.until(EC.presence_of_element_located(
            (By.NAME, "lastName"))).send_keys(last_name)
    
    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']"))).click()
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'oxd-toast')]")))
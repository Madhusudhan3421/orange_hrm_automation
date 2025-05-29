# pages/pim_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_add_employee(self):
        add_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee")))
        add_button.click()

    def open_employee_list(self):
        emp_list_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Employee List")))
        emp_list_button.click()

    def search_employee_by_name(self, name):
        search_box = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
        search_box.clear()
        search_box.send_keys(name)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def is_employee_present(self, name):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{name}']")))
            return True
        except:
            return False

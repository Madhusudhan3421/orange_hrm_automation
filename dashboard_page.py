# pages/dashboard_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_pim(self):
        pim_menu = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "PIM")))
        pim_menu.click()

    def wait_for_success_message(self):
        # Fix: Use visible toast message that contains "Successfully"
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class, 'oxd-toast') and contains(., 'Successfully')]")
            )
        )

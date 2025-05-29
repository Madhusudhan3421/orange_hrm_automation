import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sys
import os
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.add_employee_page import AddEmployeePage
from utils.driver_setup import get_driver

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_add_and_verify_employees(setup):
    driver = setup
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    pim_page = PIMPage(driver)
    add_employee_page = AddEmployeePage(driver)
    
    
    employees = [
        {"first": "madhu", "last": "sudhan"},
        {"first": "naveen", "last": "R"}
    ]
    
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    
    for emp in employees:
        dashboard_page.navigate_to_pim()
        pim_page.open_add_employee()
        add_employee_page.enter_first_name(emp["first"])
        add_employee_page.enter_last_name(emp["last"])
        add_employee_page.click_save()
        dashboard_page.wait_for_success_message()
    
    
    pim_page.open_employee_list()
    for emp in employees:
        pim_page.search_employee(emp["first"], emp["last"])
        assert pim_page.verify_employee_exists(), \
            f"Employee {emp['first']} {emp['last']} not found"
    

    dashboard_page.logout()


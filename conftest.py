import pytest
from selenium import webdriver
import os
from config import ConfigTest
from datetime import datetime
from pytest_html import extras

@pytest.fixture(scope="session", autouse=True)
def setup_directories():
    # Creating "screenshots" and "reports" folder if there is none 
            os.makedirs(
                ConfigTest.SCREENSHOT_DIR,
                exist_ok=True
            )
            os.makedirs(
                ConfigTest.REPORT_DIR,
                exist_ok=True
            )

# Opening browser for each test
@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver
# Teardown    
    driver.quit()

# Creates a report every test
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
# Checking if test is started and if it failed
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
# Creating unique file name for screenshot so it's easy to read
            timestamp = datetime.now().strftime(
                ConfigTest.TIME_DATE_FORMAT
            )
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(
                ConfigTest.SCREENSHOT_DIR,
                file_name
            )
# Creating the screenshot
            driver.save_screenshot(file_path)
# Using screenshot in the report
            if hasattr(rep, "extras"):
                rep.extras.append(extras.image(file_path))
            else:
                rep.extras = [extras.image(file_path)]
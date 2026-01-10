import pytest
from selenium import webdriver
import os
from datetime import datetime

@pytest.fixture(scope="function")

def driver(request):
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver

    if request.node.rep_call.failed:
        screenshots_dir = "screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = request.node.name
        file_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"

        driver.save_screenshot(file_path)
    
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
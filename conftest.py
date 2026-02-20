import pytest
import os
from playwright.sync_api import sync_playwright
from datetime import datetime


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=3000)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Only take screenshot if test failed during execution
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name

            screenshot_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"
            page.screenshot(path=screenshot_path)

            print(f"\n📸 Screenshot saved: {screenshot_path}")

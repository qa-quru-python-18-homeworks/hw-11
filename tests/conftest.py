import pytest
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def setup_browser():
    browser.driver.maximize_window()
    yield
    browser.quit()

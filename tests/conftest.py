import allure
import pytest
import os

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.attach import add_video
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options,
    )

    browser.config.driver = driver

    allure.step("Развернуть браузер во весь экран")(
        lambda: browser.driver.maximize_window()
    )()
    yield
    allure.step("Закрыть браузер")(lambda: browser.quit())()
    add_video(browser)

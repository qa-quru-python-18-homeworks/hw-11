import allure
import pytest
import os

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.attach import add_video, add_logs, add_html
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    with allure.step("Настройка опций браузера"):
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "128.0",
            "selenoid:options": {"enableVNC": True, "enableVideo": True},
        }
        options.capabilities.update(selenoid_capabilities)

    with allure.step("Получение данных для подключения к Selenoid"):
        selenoid_login = os.getenv("SELENOID_LOGIN")
        selenoid_pass = os.getenv("SELENOID_PASS")
        selenoid_url = os.getenv("SELENOID_URL")
        assert selenoid_login, "Не найден логин для подключения к Selenoid"
        assert selenoid_pass, "Не найден пароль для подключения к Selenoid"
        assert selenoid_url, "Не найден URL для подключения к Selenoid"

    with allure.step("Привязка драйвера к Selenoid"):
        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
            options=options,
        )
        browser.config.driver = driver

    with allure.step("Развернуть браузер во весь экран"):
        browser.driver.maximize_window()

    yield

    with allure.step("Добавление вложений"):
        add_video(browser)
        add_logs(browser)
        add_html(browser)

    with allure.step("Закрыть браузер"):
        browser.quit()

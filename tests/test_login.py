# test_login.py
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from playwright.sync_api import Page
import pytest
import allure


@allure.feature("Авторизация")
@allure.story("Авторизации недействительные учетные данные")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Авторизация с недействительными учетными данными")
def test_login_failure(login_page):
    with allure.step("Открыть страницу авторизации"):
        login_page.navigate()
    with allure.step("Ввести в форму авторизации недействительные учетные данные"):
        login_page.login("user", "password")
    with allure.step("Отображается ошибка - Invalid credentials. Please try again."):
        assert (
            login_page.get_error_message() == "Invalid credentials. Please try again."
        )
    # login_page = LoginPage(page)
    # login_page.navigate()
    # login_page.login("invalid_user", "invalid_password")
    # assert login_page.get_error_message() == "Invalid credentials. Please try again."


@allure.feature("Авторизация")
@allure.story("Авторизация корректные учетными данными")
@allure.title("Авторизация с корректными учетными данными")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    ["username", "password"], [("user", "user"), ("admin", "admin")]
)
def test_login_success(login_page, dashboard_page, username, password):
    # login_page = LoginPage(page)
    # dashboard_page = DashboardPage(page)

    # login_page.navigate()
    # login_page.login(username, password)

    # dashboard_page.asser_welcome_message(f"Welcome {username}")
    with allure.step("Открыть страницу авторизации"):
        login_page.navigate()
    with allure.step("Ввести в форму авторизации недействительные учетные данные"):
        login_page.login(username, password)
    with allure.step("Отображается приветственное сообщение с именем пользователя"):
        dashboard_page.assert_welcome_message(f"Welcome {username}")

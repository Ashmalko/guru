import pytest
from selene import browser, be, have
@pytest.fixture(
def test_valid_login():
    browser.open('https://software-testing.ru/lms/login/index.php')
    browser.element('[id="username"]').type('leha777')
    browser.element('[id="password"]').type('97916870').press_enter()
    browser.element('[id="label_1_1"]').should(have.text('Личный кабинет'))
    browser.quit()


def test_wrong_login():
    browser.open('https://software-testing.ru/lms/login/index.php')
    browser.element('[id="username"]').type('leha777')
    browser.element('[id="password"]').type('9791687.').press_enter()
    browser.element('[class="error"]').should(have.text('Неверный логин или пароль, попробуйте заново.'))
    browser.quit()
# browser.element('[id="search"]').should(have.text('QA.GURU: Курсы тестировщиков'))
from pytest import mark
from pom_pagesg.homepage import HomePage
from pom_pagesg.loginpage import LoginPage
headers = "email, password"
data = [("bill.gates@company.com", "Password123"),
            # ("hello.world@company.com", "Password123")
        ]

@mark.parametrize(headers, data)
def test_login(_driver, email, password):

    # Click on Login Link
    hp = HomePage(_driver)
    hp.home_click_login()

    lp = LoginPage(_driver)
    # Enter Email
    lp.login_enter_email("bill.gates@company.com")
    # Enter Password
    lp.login_enter_password("Password123")
    # Click Login
    lp.login_click_login()

    # hp.is_user_logged_in(email)
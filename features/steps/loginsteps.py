from behave import *
from selenium import webdriver
from configuration.config import TestData
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@Given(u'Launch the browser')
def launch_browser(context):
        
    context.service = FirefoxService(executable_path=GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=context.service)
    
@when(u'Open the https://opensource-demo.orangehrmlive.com/ website')
def open_login_page(context):
    try:
        context.driver.get(TestData.URL)
        context.loginPage = LoginPage(context.driver)
        context.dashboardPage = DashboardPage(context.driver)
    except:
        context.driver.close()
        assert False,"Test is failed in open login page section"

@then(u'The login portal has been opened')
def validate_login_page(context):
    try:
        context.loginPage.validateTitle()
    except:
        context.driver.close()
        assert False, "Test is failed in validate login page title"


@then(u'Provide the username "{user}" and password "{pwd}"')
def enter_login_creds(context, user, pwd):
    try:
        context.loginPage.enter_login_credentials(user,pwd)
    except:
        context.driver.close()
        assert False, "Test is failed in enter login credentials"


@then(u'Click on the Login button')
def enter_login(context):
    try:
        context.loginPage.enter_login()
    except:
        context.driver.close()
        assert False, "Test is failed in enter login"


@then(u'Login is successful and dashboard is opened')
def validate_dashboard_page(context):
    try:
        context.dashboardPage.validatePageLoaded()
    except:
        context.driver.close()
        assert False, "Test is failed in validating dashboard"

@then(u'Login is failed and invalid credential error is displayed')
def validate_invalid_login(context):
    try:
        context.loginPage.validateInvalidCreds()
    except:
        context.driver.close()
        assert False, "Test is failed in validating invalid login"

@then(u'Provide the password "{pwd}"')
def enter_login_cred(context, pwd):
    try:
        context.loginPage.enter_password(pwd)
    except:
        context.driver.close()
        assert False, "Test is failed in enter password"

@then(u'Provide the username "{user}"')
def enter_login_creds(context, user):
    try:
        context.loginPage.enter_username(user)
    except:
        context.driver.close()
        assert False, "Test is failed in enter username"

@then(u'Login is failed and empty username error is displayed')
def validate_empty_username(context):
    try:
        context.loginPage.validateEmptyUsername()
    except:
        context.driver.close()
        assert False, "Test is failed in validate empty username"

@then(u'Login is failed and empty password error is displayed')
def validate_empty_password(context):
    try:
        context.loginPage.validateEmptyPassword()
    except:
        context.driver.close()
        assert False, "Test is failed in validate empty password"



@then(u'Close the browser')
def step_impl(context):
    context.driver.close()
    context.driver.quit()
from behave import *

from web_utils.web_functions import Browser
import web_utils.constants as constants


@given(u'the user has the correct credentials')
def step_impl(context):
    context.driver = Browser.GoTo.go_to_page(constants.URL)


@when(u'the user enters username')
def step_impl(context):
    """Allows the username to be entered"""
    Browser.Fields.add_username_to_field(context.driver, constants.USERNAME)


@when(u'the user enters password')
def step_impl(context):
    """Allows the password to be entered"""
    Browser.Fields.add_password_to_field(context.driver, constants.PASSWORD)


@when(u'clicks Login')
def step_impl(context):
    """Clicks the login button for the given page"""
    Browser.Click.login_button(context.driver)


@then(u'the user is presented with a welcome message')
def step_impl(context):
    """Checks if the user is presented with a welcome message"""
    Browser.Page.verify_if_curr_page_is_on_welcome_page(context.driver)
    context.driver.quit()

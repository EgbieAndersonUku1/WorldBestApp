from behave import *

from web_utils.web_functions import Browser
import web_utils.constants as constants


@given(u'we have a user')
def step_impl(context):
    context.driver = Browser.GoTo.go_to_page(constants.URL)


@when(u'the user enters the "{username}" username')
def step_impl(context, username):
    Browser.Fields.add_username_to_field(context.driver, username)


@when(u'the user enters the "{password}" password')
def step_impl(context, password):
    Browser.Fields.add_password_to_field(context.driver, password)


@when(u'user clicks Login')
def step_impl(context):
    Browser.Click.login_button(context.driver)


@then(u'user is presented with a error message')
def step_impl(context):
    Browser.Page.verify_error_message_for_incorrect_credentials(context.driver)
    context.driver.quit()


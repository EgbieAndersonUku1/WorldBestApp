from selenium import webdriver

from page_object.login import web_elements
from page_object.welcome_page import locators
from web_utils import web_common


class Browser(object):

    class GoTo(object):
        """The GoTo class allows the Browser to travel to any page providing a valid URL is given"""

        @classmethod
        def go_to_page(cls, url, browser_type=None):
            """go_to_page(str, str) -> returns selenium driver object

               The method takes a url and a browser type(default value is None) i.e Firefox, Chrome, etc
               and allows the browser to traverse to that page.

               :param url : The url that the browser will go to.
               :param browser_type: The type of browser to be used with the selenium object i.e. Firefox
                                    The default is None
               :return: A selenium driver
            """
            driver = cls._check_browser_type(browser_type)
            driver.get(url=url.strip())

            return driver

        @classmethod
        def _check_browser_type(cls, browser_type):
            """_check_browser_type(str) -> return selenium driver obj or raise Error message

               Takes a string parameter a browser type and providing the browser type
               exists allows the selenium driver to open that browser. If that browser
               is not found an exception message is raised. The default browser is Chrome.

               :param browser_type: The browser that will be opened by the selenium driver. Default
                                    browser is Chrome.
               :return: A driver object.
            """
            if browser_type is None:
                driver = webdriver.Chrome()
            elif browser_type.lower() == "firefox":
                driver = webdriver.Firefox()
            elif browser_type.lower() == "safari":
                driver = webdriver.Safari()
            else:
                raise Exception("The browser <{}> is not supported".format(browser_type.title()))
            return driver

    class Fields(object):
        """This class allows the browser access the form fields of the page"""

        @classmethod
        def add_username_to_field(cls, driver, username):
            """add_username_to_field(selenium obj, str) -> return None

              :param driver: The selenium driver that allows the browser and the elements of web page
                             to be accessed.
              :param username: The username value for the username field.
            """
            username_elem = Browser._FieldHelper.find_element(driver, xpath=web_elements.username)
            cls._send_field_value(username_elem, field_value=username)

        @classmethod
        def add_password_to_field(cls, driver, password):
            """add_password_to_field(selenium obj, str) -> return None

            :param driver: The selenium driver that allows the browser and the elements of the
                            web page to be accessed.
            :param password: The password value for password field.
            """
            password_elem = Browser._FieldHelper.find_element(driver, xpath=web_elements.password)
            cls._send_field_value(field=password_elem, field_value=password)

        @classmethod
        def _send_field_value(cls, field, field_value):
            """_send_field_value(element obj, str) -> returns None

               Sends the value to required form fields

               :param field: A field element that represents a form field
               :param field_value: The value that will be entered in the form field.
            """
            field.send_keys(field_value)

    class Click(object):
        """The class allows the Browser to click on the various button on the page"""

        @staticmethod
        def login_button(driver):
            """login_button(selenium object) -> return None

               The login in button for the page. When clicked providing the username
               and password is correct takes the user to the landing page or displays
               an error

               :param driver: The selenium driver that allows the browser and the elements of
                              the web page to be accessed.
            """
            login_button = Browser._FieldHelper.find_element(driver, xpath=web_elements.login_button)
            login_button.click()

    class Page(object):
        """Allows the various attributes of a page to be accessed"""

        @staticmethod
        def verify_if_curr_page_is_on_welcome_page(driver):
            """verify_if_curr_page_is_on_welcome_page(selenium driver obj) -> returns None

               Checks if the current page the browser is the welcome page. Returns None
               if the current page is equal welcome page else assert an error.

               :param driver: The selenium driver that allows the browser and the elements of
                              the web page to be accessed.
            """
            page_elem_dict = locators.elements
            page = Browser._FieldHelper.find_element(driver, xpath=page_elem_dict.get("welcome_message_path"))

            assert page.text == page_elem_dict.get("welcome_message")

        @staticmethod
        def verify_error_message_for_incorrect_credentials(driver):
            """verify_error_message_for_incorrect_credentials(selenium obj) -> returns None

               Checks if an error message is returned if the user enters incorrect credentials.

               :param driver: The selenium driver that allows the browser and the elements of
                              the web page to be accessed.
            """
            login_error = web_elements.login_error
            page = driver.find_element_by_id(login_error.get("error_message_id"))
            web_common.is_element_visible(page)
            assert page.text == login_error.get("error_message")

    class _FieldHelper(object):
        """A helper class that provides help to the classes"""

        @classmethod
        def find_element(cls, driver, xpath):
            """field_helper(selenium obj, str) -> returns field xpath

               Takes a selenium driver and xpath and attempts to find
               the element for that xpath. If found returns web element
               else an error is raised.

               :param driver: The selenium driver that allows the browser and the elements of
                              the web page to be accessed.
               :param: xpath: The xpath for the given element to be find.
            """
            field = driver.find_element_by_xpath(xpath)
            web_common.is_element_visible(field)
            return field


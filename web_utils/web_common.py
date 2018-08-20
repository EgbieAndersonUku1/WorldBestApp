

def is_element_visible(element):
    """is_element_visible( web obj element) -> returns None or Error

       Takes a web element as parameter and checks if that element
       is visible on the page. If that element is visible returns None
       else raise an AssertionError.

       :param element: The element to be checked.

    """
    if not element.is_displayed():
        AssertionError("The element could not be found!")
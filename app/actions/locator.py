"""A module for locating an element on the page using the playwright API."""

import playwright.sync_api as Playwright

def locate(page: Playwright, locate_info: dict[str, object]) -> Playwright.ElementHandle:
    """for locating an element on the page

    This function locates an element on the page using the playwright API.
    Based on the information in the locate_info dictionary, the function will use the appropriate method to locate the element.

    Args:
        page: The playwright page object.
        locate_info: The information to locate the element.

    Returns:
        The playwright element handle of the located element.
    """
    
    by = locate_info['locate']['by']
    by_value = locate_info['locate']['byValue']
    if by == "CSS_SELECTOR" or by == "XPATH" or by == "NAME":
        return page.locator(by_value)

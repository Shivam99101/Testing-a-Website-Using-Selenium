from locater import *
from element import BassPageElement

class SearchTextElement(BassPageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = "q"

class BassPage(object):
    """Base class to initialize the base page that will be called from all
    pages"""
# Not necessarily need 'object' as inheritance.
    def __init__(self,driver):
        self.driver = driver

# Whichever webpage we want to test, we'll define a class for that webpage.
# For example, if we want test a homepage and a search page, we'll add class Homepage and class searchpage.
# We will inherit from Basepage.

class MainPage(BassPage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultsPage(BassPage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page element, but as for now it works fine
        return "No results found." not in self.driver.page_source
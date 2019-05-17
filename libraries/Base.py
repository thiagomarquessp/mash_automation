from SeleniumLibrary import SeleniumLibrary
from robot.libraries.BuiltIn import BuiltIn


class Base(object):

    def __init__(self):
        self.builtin_lib = BuiltIn()
        self.selenium_lib = SeleniumLibrary()

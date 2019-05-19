from libraries.TestSetup import TestSetup
from libraries.WebKeywords import WebKeywords


class PyKeywords(
    TestSetup,
    WebKeywords
):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

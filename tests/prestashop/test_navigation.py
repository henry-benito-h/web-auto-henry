from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.prestashop.landing_page import LandingPage
from pages.prestashop.header_page import HeaderPage
from utils.logger import get_logger


logger = get_logger(__name__)
class TestPrestashopLandingPage:
    
    @classmethod
    def setup_class(self):
        # start the session
        self.driver = webdriver.Chrome()
        logger.info("Starting the session")
        self.driver.implicitly_wait(10)
    
    def test_navigate_to_accesories(self):
        """
        Test navigation to Accessories page and verify breadcrumb
        """        
        
        # create the page object
        landing_page = LandingPage(self.driver)
        header_page = HeaderPage(self.driver)
        header_page.click_accesories()

        assert "Accessories" in landing_page.get_breadcrumb().text, "Breadcrumb does not contain expected text"

    @classmethod
    def teardown_class(self):
        # Close the browser
        logger.info("Closing the browser")
        self.driver.quit()
        
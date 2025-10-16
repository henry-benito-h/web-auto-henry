from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utils.logger import get_logger
from pages.prestashop.selenium.base_page import BasePage

logger = get_logger(__name__)

class LandingPage(BasePage):

    loading = (By.ID, "loadingMessage")
    breadcrumb_home = (By.CSS_SELECTOR, "section#wrapper nav.breadcrumb ol")
    elements_option = (By.XPATH, "//h5[text()='Elements']")
    forms_option = (By.XPATH, "//h5[text()='Forms']")    
    alerts_frames_windows_option = (By.XPATH, "//h5[text()='Alerts, Frame & Windows']")    
    
    def __init__(self, driver):
        super().__init__(driver)        
        self.url = "https://demo.prestashop.com/"
        self.driver.get(self.url)
        logger.info("Navigating to the page: " + self.url)

    def wait_loading_message(self):
        self.find_element(self.loading)
        self.wait_disappears_element(self.loading)

    def get_breadcrumb(self):
        return self.find_element(self.breadcrumb_home)
    
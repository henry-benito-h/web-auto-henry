from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utils.logger import get_logger
from pages.prestashop.selenium.base_page import BasePage

logger = get_logger(__name__)

class HeaderPage(BasePage):

    # locators
    clothes_menu_item = (By.CSS_SELECTOR, "li#category-3 a span")
    accesories_menu_item = (By.CSS_SELECTOR, "li#category-6 a")
    art_menu_item = (By.CSS_SELECTOR, "li#category-9 a span")
    search_input = (By.NAME, "s")

    def __init__(self, driver):
        super().__init__(driver)
        self.switch_to_frame("framelive")

    def click_clothes(self):
        self.click_element(self.clothes_menu_item, waitForClickable=True, through_js=True)
    
    def click_accesories(self):
        self.click_element(self.accesories_menu_item, waitForClickable=True, through_js=True)
    
    def click_art(self):
        self.click_element(self.art_menu_item, waitForClickable=True, through_js=True)
        

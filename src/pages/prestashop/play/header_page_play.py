from playwright.sync_api import Page, Locator
import logging
from utils.logger import get_logger
from pages.prestashop.play.base_page_play import BasePagePlay

logger = get_logger(__name__)

class HeaderPagePlay(BasePagePlay):

    # locators
   

    def __init__(self, page: Page):
        self.page = page
        self.clothes_menu_item : Locator = page.locator("li#category-3 a")
        self.accesories_menu_item : Locator = page.locator("li#category-6 a")
        self.art_menu_item : Locator = page.locator("li#category-9 a")
        self.search_input = page.locator("input[name='s']")
        # Switch to frame
        self.frame = self.switch_to_frame("framelive")

    def click_clothes(self):
        self.frame.click("li#category-3 a")
    
    def click_accesories(self):
        self.frame.click("li#category-6 a")
    
    def click_art(self):
        self.frame.click("li#category-9 a")

    def click_menu(self, menu_name: str) -> None:
            menu_name = menu_name.lower()
            if menu_name == "clothes":
                self.click_clothes()
            elif menu_name == "accessories":
                self.click_accesories()
            elif menu_name == "art":
                self.click_art()
            else:
                raise ValueError(f"Menu '{menu_name}' not recognized. Available menus: clothes, accessories, art.")


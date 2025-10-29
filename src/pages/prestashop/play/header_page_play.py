from playwright.sync_api import Page, Locator
import logging
from utils.logger import get_logger
from pages.prestashop.play.base_page_play import BasePagePlay

logger = get_logger(__name__)

class HeaderPagePlay(BasePagePlay):

    def __init__(self, page: Page):
        self.page = page
        self.clothes_menu_item = "li#category-3 a"
        self.accesories_menu_item = "li#category-6 a"
        self.art_menu_item = "li#category-9 a"
        self.search_input = page.locator("input[name='s']")
        # Switch to frame
        self.frame = self.switch_to_frame("framelive")

    def get_menu_locators(self):
        return {
            "clothes": self.clothes_menu_item,
            "accessories": self.accesories_menu_item,
            "art": self.art_menu_item,
        }
    
    def click_menu(self, menu_name: str) -> None:
            """Click on menu item based on menu name
            Args:
                menu_name (str): Name of the menu item to click (clothes, accessories, art)
            Raises:
                ValueError: If menu_name is not recognized
            """
            if menu_name.lower() in self.get_menu_locators():
                self.frame.click(self.get_menu_locators()[menu_name.lower()])
                logger.info(f"Clicking on '{menu_name}' menu item")
            else:
                raise ValueError(f"Menu '{menu_name}' not recognized. Available menus: {list(self.get_menu_locators().keys())}")

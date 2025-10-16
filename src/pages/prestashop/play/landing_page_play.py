from playwright.sync_api import Page, Locator
from pages.prestashop.play.base_page_play import BasePagePlay
from pages.prestashop.play.header_page_play import HeaderPagePlay

class LandingPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.loading : Locator = page.locator("#loadingMessage")
        self.breadcrumb_home : Locator = page.locator("section#wrapper nav.breadcrumb ol")
        self.product_list_header : Locator = page.locator("div#js-product-list-header")

    def navigate(self):
        self.navigate_url("https://demo.prestashop.com/")

    def move_to_menu(self, menu_name):
        HeaderPagePlay(self.page).click_menu(menu_name)
        self.product_list_header.get_by_text(menu_name)

    def get_breadcrumb(self):
        self.frame = self.switch_to_frame("framelive")
        return self.frame.locator("section#wrapper nav.breadcrumb ol")
    


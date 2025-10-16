import re
import time

from playwright.sync_api import Page, expect
import pytest
from pages.prestashop.play.landing_page_play import LandingPagePlay

class TestElementsPagePlay:

    @pytest.mark.parametrize("menu", ["Accessories","Clothes", "Art"])
    def test_navigate_to_menus(self, page: Page, menu: str) -> None:
        landing_page = LandingPagePlay(page)
        landing_page.navigate()
        landing_page.move_to_menu(menu)
        time.sleep(5)
        assert menu in landing_page.get_breadcrumb().text_content(), "Breadcrumb does not contain expected text"
        expect(landing_page.get_breadcrumb()).to_contain_text(menu)

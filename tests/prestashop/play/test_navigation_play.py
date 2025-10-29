import re
import time

from playwright.sync_api import Page, expect
import pytest
from soft_assert import check
from soft_assert import verify
from pages.prestashop.play.landing_page_play import LandingPagePlay

class TestElementsPagePlay:


    @pytest.mark.parametrize("read_data", ["menus"], indirect=True)
    def test_navigate_to_menus(self, page: Page, read_data, log_test_name) -> None:
        """
        Test navigation to different menus and verify breadcrumbs
        Args:
            page (Page): Playwright Page object
            read_data (list): List of dictionaries with menu data
        Raises:
            AssertionError: If breadcrumb does not contain expected menu name
        """
        landing_page = LandingPagePlay(page)
        with verify():
            for data in read_data:
                landing_page.navigate()
                landing_page.move_to_menu(data["menu"])
                time.sleep(5)
                check(
                        data["menu"] in landing_page.get_breadcrumb().text_content(),
                        f"{data['menu']} breadcrumb does not contain expected text",
                    )

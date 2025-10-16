import time
from playwright.sync_api import Page
from utils.logger import get_logger
logger = get_logger(__name__)

class BasePagePlay(Page):
    def __init__(self, page: Page):
        self.page = page
    
    def navigate_url(self, url):
        logger.info(f"Navigating to: {url}")
        self.page.goto(url)

    def wait_disappears_element(self, by_locator, timeout=30):
        logger.info(f"Wait until disappears element:  {by_locator}")
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(by_locator)) #TODO: Update for Playwright

    def click_element(self, locator):
        """Click on element"""                                
        tag_name, element_name = self.get_tag_and_text(locator)
        logger.info(f"Clicking on {element_name} element: {tag_name}")
        locator.click()
    
    def enter_text(self, locator, text):
        """Enter text into input field"""      
        tag_name, element_name = self.get_tag_and_text(locator)  
        logger.info(f"Entering text '{text}' into {element_name} element: {tag_name}")
        locator.fill(text)
    
    def get_tag_and_text(self, locator):
        """Get tag name and text from locator"""
        # get the tag from locator: button, span, div, a, etc.
        tag_name = locator.evaluate("node => node.tagName")
        # get the text from locator | text_content | inner_text
        if locator.inner_text():
            element_name = locator.inner_text()
        else:
            element_name = tag_name
        return tag_name, element_name

    def highlight(self, element, effect_time=2, color="blue", border=5):
        """
        Highlights (blinks) a Selenium Webdriver element
        """
        def apply_style(s):
            self.page.evaluate("arguments[0].setAttribute('style', arguments[1]);", element, s)

        original_style = self.page.evaluate("arguments[0].getAttribute('style');", element)
        apply_style("border: {0}px solid {1};".format(border, color))
        time.sleep(effect_time)
        apply_style(original_style)

    def switch_to_frame(self, identifier):
        iframe_element = self.page.wait_for_selector(f"iframe[name='{identifier}']")
        frame = iframe_element.content_frame()

        frame.wait_for_load_state("domcontentloaded")
        logger.info(f"Switching to frame:  {identifier}")
        return frame

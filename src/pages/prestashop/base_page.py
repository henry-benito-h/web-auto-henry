from selenium.webdriver.common.by import By
import time
import logging
from utils.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger(__name__)


class BasePage:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(self.driver, 10)
	
	def find_element(self, by_locator, timeout=30):
		logger.info(f"Finding element:  {by_locator}")
		return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))

	def wait_disappears_element(self, by_locator, timeout=30):
		logger.info(f"Wait until disappears element:  {by_locator}")
		return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(by_locator))


	def click_element(self, by_locator, waitForClickable=False, through_js=False):
		self.highlight(self.driver, self.find_element(by_locator))
		if waitForClickable:
			WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator))
		if through_js:
			self.driver.execute_script("arguments[0].click();", self.find_element(by_locator))	
			logger.info(f"Clicking element through JS:  {by_locator}")
		else:
			self.find_element(by_locator).click()
			logger.info(f"Clicking element:  {by_locator}")
	
	def click_element_js(self, by_locator, waitForClickable=False):
		self.highlight(self.driver, self.find_element(by_locator))
		if waitForClickable:
			WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator))	
		else:
			self.find_element(by_locator).click()
		self.driver.execute_script("arguments[0].click();", self.find_element(by_locator))

		
	

	def enter_text(self, by_locator, text):         
		self.find_element(by_locator).send_keys(text)
		logger.info(f"Entering text:  {text} on {by_locator}")
	
	def highlight(self, driver, element, effect_time=2, color="blue", border=5):
		"""
		Highlights (blinks) a Selenium Webdriver element
		"""
		def apply_style(s):
			driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
		
		original_style = element.get_attribute('style')
		apply_style("border: {0}px solid {1};".format(border, color))
		time.sleep(effect_time)
		apply_style(original_style)

	def switch_to_frame(self, identifier):
		WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it(identifier))	
		logger.info(f"Switching to frame:  {identifier}")
		
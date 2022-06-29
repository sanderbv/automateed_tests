from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


# the class for the base page (base page is using for the configuration, like config.js in QMate)
class BasePage:

    # function to create a driver and url
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # function to open browser with url
    def open(self):
        self.driver.get(self.url)

    # function to wait and find an element on the page
    def element_is_visible(self, locator, timeout=3):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # function to wait and find elements on the page
    def elements_are_visible(self, locator, timeout=3):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    # function to remove footer and adv, make submit button is visible
    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('adplus-anchor').remove()")

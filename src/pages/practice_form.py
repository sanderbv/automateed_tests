from src.pages.base_page import BasePage
from src.locators.practice_form import PracticeFormLocators as Locators
import json


with open('../src/data/testdata.json') as file:
    data = json.load(file)


class PracticeFormPage(BasePage):
    def fill_out_fields_submit(self):
        self.remove_footer()
        self.element_is_visible(Locators.firstName).send_keys(data["StudentRegistrationForm"][0]['FirstName'])
        self.element_is_visible(Locators.lastName).send_keys(data["StudentRegistrationForm"][0]['LastName'])
        self.element_is_visible(Locators.email).send_keys(data["StudentRegistrationForm"][0]['Email'])
        self.element_is_visible(Locators.gender).click()
        self.element_is_visible(Locators.mobile).send_keys(data["StudentRegistrationForm"][0]['Mobile'])
        # self.element_is_visible(Locators.subject).send_keys('English')
        self.element_is_visible(Locators.hobbies).click()
        self.element_is_visible(Locators.currentAddress).send_keys(data["StudentRegistrationForm"][0]['Mobile'])
        self.element_is_visible(Locators.submit).click()
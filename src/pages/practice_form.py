from src.data.convert_td import generated_person
from src.pages.base_page import BasePage
from src.locators.practice_form import PracticeFormLocators as Locators


class PracticeFormPage(BasePage):
    def fill_out_fields_submit(self):
        self.remove_footer()
        person = generated_person()
        self.element_is_visible(Locators.firstName).send_keys(person.FirstName)
        self.element_is_visible(Locators.lastName).send_keys(person.LastName)
        self.element_is_visible(Locators.email).send_keys(person.Email)
        self.element_is_visible(Locators.gender).click()
        self.element_is_visible(Locators.mobile).send_keys(person.Mobile)
        # self.element_is_visible(Locators.subject).send_keys('English')
        self.element_is_visible(Locators.hobbies).click()
        self.element_is_visible(Locators.currentAddress).send_keys(person.Address)
        self.element_is_visible(Locators.submit).click()
        return person

    def form_result(self):
        result_list = self.elements_are_visible(Locators.resultTable)
        result_table = [i.text for i in result_list]
        return result_table

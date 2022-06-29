from src.pages.practice_form import PracticeFormPage


class TestPracticeForm:

    def test_form(self, driver):
        form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        form_page.fill_out_fields_submit()

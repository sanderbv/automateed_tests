from src.pages.practice_form import PracticeFormPage


# create class to test the Practice Form page
class TestPracticeForm:

    # function to open browser and execute testing
    def test_form(self, driver):
        # provide the page and link for testing
        form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
        # open the Practice Form page
        form_page.open()
        # fill in the requirement fields and return filled data for person
        person = form_page.fill_out_fields_submit()
        # return data from submitted form
        result_table = form_page.form_result()
        # check submitted form
        for rv in result_table:
            # check Student Name
            if f'Student Name {person.FirstName} {person.LastName}' == rv:
                assert f'Student Name {person.FirstName} {person.LastName}' == rv
            # check Student Email
            elif f'Student Email {person.Email}' == rv:
                assert f'Student Email {person.Email}' == rv
            # check Student Mobile
            elif f'Mobile {person.Mobile}' == rv:
                assert f'Mobile {person.Mobile}' == rv

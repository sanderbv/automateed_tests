from selenium.webdriver.common.by import By
from random import randint


# Locators on the Practice Form page
class PracticeFormLocators:

    # input fields
    firstName = (By.CSS_SELECTOR, '#firstName')
    lastName = (By.CSS_SELECTOR, '#lastName')
    email = (By.CSS_SELECTOR, '#userEmail')
    mobile = (By.CSS_SELECTOR, '#userNumber')
    subject = (By.CSS_SELECTOR, '#subjectsInput')
    currentAddress = (By.CSS_SELECTOR, '#currentAddress')

    # checkbox/radiobutton
    gender = (By.CSS_SELECTOR, f"label[for='gender-radio-{randint(1, 3)}']")
    hobbies = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{randint(1, 3)}']")

    # file menu
    fileInput = (By.CSS_SELECTOR, '#uploadPicture')

    # buttons
    submit = (By.CSS_SELECTOR, '#submit')

    # get result table
    resultTable = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
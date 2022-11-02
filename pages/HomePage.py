from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):
    header = (By.XPATH, '//strong[text() = "KİTABEVİM.AZ"]')
    search_line = (By.XPATH, "//*[@class = 'ts-search-by-category hidden-ipad']//input[@placeholder]")
    username = (By.ID, "txtUsername")
    password = (By.ID, "txtPassword")
    button = (By.NAME, "Submit")
    forgot = (By.XPATH, "//*[@cla = 'oxd-text oxd-text--p orangehrm-login-forgot-header']")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def load_home_page(self):
        self.open_home_page(self.header)

    def search_using_csv(self):
        file = open("../tests/search.csv")
        input_search = file.read()
        self.input_text(self.search_line, input_search)

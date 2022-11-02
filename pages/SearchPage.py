import random
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class SearchPage(BasePage):
    book_name = (By.XPATH, "//h3//a")
    stock_status = (By.XPATH, "//*[contains(@class, 'availability')]//span")

    def __init__(self, driver):
        super(SearchPage, self).__init__(driver)

    def select_random_book(self):
        books = []
        name = self.driver.find_elements(*self.book_name)
        for value in name:
            books.append(value.text)

        self.do_click((By.XPATH, f"//*[text() = '{random.choice(books)}']"))
        self.is_visible(self.stock_status)
        while True:
            if self.driver.find_element(*self.stock_status).text == 'ANBARDA':
                break
            self.driver.back()
            self.do_click((By.XPATH, f"//*[text() = '{random.choice(books)}']"))

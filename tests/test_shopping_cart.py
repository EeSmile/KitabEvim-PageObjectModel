from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from pages.BookPage import BookPage
from pages.CartPage import CartPage

url = "https://kitabevim.az/"


def test_shopping_cart(init_driver):
    home_page = HomePage(init_driver)
    book_page = BookPage(init_driver)
    cart_page = CartPage(init_driver)

    home_page.load_home_page()
    home_page.search_using_csv()

    search_page = SearchPage(init_driver)
    search_page.select_random_book()

    assert book_page.add_to_cart() == "1", \
        f"the value of the trash icon in the upper right corner of the web page has not changed to the number '1'"

    book_page.basket_hover()
    book_page.view_shopping_cart()

    cart_page.increase_by_one()
    assert cart_page.reload_cart() == "Səbət yeniləndi.", "The message 'Səbət yeniləndi.' is notdisplayed."

    cart_page.click_cross()
    assert cart_page.check_basket() == "Səbətiniz hazırda boşdur.", "The basket is not empty"
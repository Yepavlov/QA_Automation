from page_object.pages.cart_page import CartPage
from page_object.pages.products_page import Products


def test_check_added_goods_from_the_page_goods(logged_in_main_page):
    products_page = Products(logged_in_main_page.driver)
    products_page.click_product("Sauce Labs Backpack")
    products_page.add_product_to_card("sauce-labs-backpack")
    products_page.go_to_cart()
    cart_page = CartPage(logged_in_main_page.driver)
    cart_page.check_added_goods(["Sauce Labs Backpack"])


def test_check_remove_from_the_cart(logged_in_main_page):
    products_page = Products(logged_in_main_page.driver)
    products_page.click_product("Sauce Labs Backpack")
    products_page.add_product_to_card("sauce-labs-backpack")
    products_page.go_to_cart()
    cart_page = CartPage(logged_in_main_page.driver)
    cart_page.remove_from_the_cart("sauce-labs-backpack")
    cart_page.check_remove_good("Sauce Labs Backpack")


def test_check_some_added_products(logged_in_main_page):
    products_page = Products(logged_in_main_page.driver)
    products_page.add_product_to_card("sauce-labs-bike-light")
    products_page.add_product_to_card("sauce-labs-fleece-jacket")
    products_page.go_to_cart()
    cart_page = CartPage(logged_in_main_page.driver)
    cart_page.check_added_goods(["Sauce Labs Bike Light", "Sauce Labs Fleece Jacket"])


def test_check_fill_in_your_information(logged_in_main_page):
    products_page = Products(logged_in_main_page.driver)
    products_page.add_product_to_card("sauce-labs-onesie")
    products_page.add_product_to_card("test\.allthethings\(\)-t-shirt-\(red\)")
    products_page.go_to_cart()
    cart_page = CartPage(logged_in_main_page.driver)
    cart_page.check_added_goods(
        ["Test.allTheThings() T-Shirt (Red)", "Sauce Labs Onesie"]
    )
    cart_page.click_button_ckeckout()
    cart_page.fill_in_your_information("Yevhenii", "Pavlov", "2400")


def test_the_total_price(logged_in_main_page):
    products_page = Products(logged_in_main_page.driver)
    products_page.add_product_to_card("sauce-labs-onesie")
    products_page.add_product_to_card("test\.allthethings\(\)-t-shirt-\(red\)")
    products_page.add_product_to_card("sauce-labs-bike-light")
    products_page.go_to_cart()
    cart_page = CartPage(logged_in_main_page.driver)
    cart_page.check_added_goods(
        [
            "Test.allTheThings() T-Shirt (Red)",
            "Sauce Labs Onesie",
            "Sauce Labs Bike Light",
        ]
    )
    cart_page.click_button_ckeckout()
    cart_page.fill_in_your_information("Yevhenii", "Pavlov", "2400")
    cart_page.check_the_correct_total()

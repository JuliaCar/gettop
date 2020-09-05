from behave import given, when, then


@given('Open GetTop home page')
def open_get_top(context):
    context.app.page.open_page()


@when('Click on the shopping cart icon')
def shopping_cart_open(context):
    context.app.top_nav_menu_page.shopping_cart_icon_click()


@then('Page contains {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.app.shopping_cart_page.verify_cart_empty_text(search_word)


@when('Hover over the shopping cart icon')
def hover_over_shopping_cart(context):
    context.app.top_nav_menu_page.hover_over_shopping_cart()


# @when('Move to the shopping cart icon')
# def move_shopping_cart_icon(context):
#     context.app.top_nav_menu_page.move_shopping_cart_icon()


@then('Click on "Checkout" button')
def checkout_btn_click_top_menu(context):
    context.app.top_nav_menu_page.checkout_btn_click()


@then('Verify that user can click on "Checkout" button')
def checkout_btn_click(context):
    context.app.top_nav_menu_page.checkout_btn_click()


@then('It takes to {correct_page} page')
def verify_checkout_page(context, correct_page):
    context.app.product_page.verify_checkout_page(correct_page)


@then('Message {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.app.top_nav_menu_page.verify_cart_empty_text(search_word)


@given('Open product {product_id} page')
def open_product_id_page(context, product_id):
    context.driver.get(f'https://www.gettop.us/product/{product_id}/')


@when('Click on ADD TO CART button')
def add_product_to_cart(context):
    context.app.product_page.add_product_to_cart()


@then('Verify that price in top nav menu cart is correct')
def verify_price(context):
    context.app.top_nav_menu_page.verify_topmenu_cart_same_price()


@when('User open other product page')
def open_product_page_top_menu(context):
    context.app.top_nav_menu_page.open_products_page_topmenu()
    context.app.top_nav_menu_page.open_product_page_topmenu()


@when('Add second product to the cart')
def add_second_product_to_cart(context):
    context.app.product_page.add_second_product_to_cart()


@then('Verify that {amount} items in cart')
def verify_amount_items_topmenu_cart(context, amount):
    context.app.top_nav_menu_page.verify_amount_items_topmenu_cart(amount)


@then('Verify that {total_price} price shown')
def subtotal_shown_top_cart(context, total_price):
    context.app.top_nav_menu_page.price_subtotal_shown_top_cart(total_price)


@then('Verify {product_1} and {product_2} in the cart')
def products_in_cart(context, product_1, product_2):
    context.app.top_nav_menu_page.products_in_cart(product_1, product_2)


@then('Verify can click on View Cart')
def click_view_cart_btn(context):
    context.app.top_nav_menu_page.click_view_cart_btn()


@then('User can remove product')
def remove_from_cart_btn(context):
    context.app.top_nav_menu_page.remove_from_cart_btn()

from behave import given, when, then
from time import sleep


@given('Open GetTop {category} category page')
def open_category_page(context, category):
    context.app.category_page.open_category_page(category)

@then('Verify items of {category_name} category are shown')
def correct_category_items_shown(context, category_name):
    context.app.category_page.correct_category_items_shown(category_name)

@then('Verify {shown_results_text} is present')
def shown_results_text_present(context, shown_results_text):
    context.app.category_page.shown_results_text_present(shown_results_text)

@then('Verify that {amount} items are present')
def correct_amount_items_present(context, amount):
    context.app.category_page.correct_amount_items_present(amount)

@then('Verify that all items have Category, Name and Price')
def items_category_name_price(context):
    context.app.category_page.items_category_name_price()

@then('Verify user can open Quick View')
def user_open_quick_view(context):
    context.app.category_page.user_open_quick_view()
    context.app.home_page.verify_quick_view_open()


@then('User can add products to cart in Quick View')
def add_product_cart(context):
    context.app.category_page.add_product_cart_quck_view()

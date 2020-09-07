from behave import when, then
from time import sleep


@then('Verify that item added to the shopping cart')
def item_added_to_cart(context):
    context.app.product_page.item_added_to_cart()

@when('Click {plus_minus_sign} button {amount_times} times')
def click_plus_or_minus_button(context, plus_minus_sign, amount_times):
    context.app.product_page.click_plus_or_minus_button(plus_minus_sign, amount_times)

@when('User can type in {amount} amount of items to add to cart')
def input_amount_items_add_window(context, amount):
    context.app.product_page.input_amount_items_add_window(amount)

@then('Verify user sees "...have been added to your cart" message confirmation')
def text_confirmation_added_cart(context):
    context.app.product_page.item_added_to_cart()

@then('Verify user sees {text} message')
def out_of_stock(context, text):
    context.app.product_page.our_of_stock(text)
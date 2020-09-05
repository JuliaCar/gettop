from behave import when, then


@when('Search for {product_name} product')
def search_for_product(context, product_name):
    context.app.top_nav_menu_page.hover_over_search_window(product_name)


@then('Verify user see {product_name} product page')
def open_correct_product_page(context, product_name):
    context.app.product_page.open_correct_product_page(product_name)


@then('Verify user see {notification_no_product} on page')
def notification_no_product(context, notification_no_product):
    context.app.product_page.notification_no_product(notification_no_product)

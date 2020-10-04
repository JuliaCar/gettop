from behave import given, when, then


@given('Open GetTop {name_page} page')
def open_shop_page(context, name_page):
    context.app.shop_page.open_shop_page(name_page)

@then('Verify user see {amount_items} recently viewed items')
def recently_viewed_items_present(context, amount_items):
    context.app.shop_page.recently_viewed_items_present(amount_items)

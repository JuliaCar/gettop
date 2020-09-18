from behave import then

@then('User can sort products by price: high to low')
def sorting_by_price_desc(context):
    context.app.shop_page.sorting_by_price_desc()

@then('User can sort products by price: low to high')
def sorting_by_price(context):
    context.app.shop_page.sorting_by_price()

@then('User can sort products by popularity')
def sorting_by_popularity(context):
    context.app.shop_page.sorting_by_popularity()

@then('User can sort products by rating')
def sorting_by_rating(context):
    context.app.shop_page.sorting_by_rating()

@then('User can sort products by latest')
def sorting_by_latest(context):
    context.app.shop_page.sorting_by_latest()

from behave import when, then


@then('Verify {text_shown} text is shown')
def text_is_shown(context, text_shown):
    context.app.home_page.text_is_shown(text_shown)


@then('Verify user can click on heart icon')
def click_heart_icon(context):
    context.app.home_page.click_heart_icon()


@when('Verify that every product has all icons')
def sales_product_all_icons(context):
    context.app.home_page.sales_product_all_icons()


@when('Open product from Sale')
def open_product_sale(context):
    context.app.home_page.open_product_sale()


@then('Verify that user can see price and description')
def price_description_shown(context):
    context.app.product_page.price_description_shown()


@then('Verify that user can open Quick View')
def open_quick_view(context):
    context.app.home_page.open_quick_view()


@then('Verify that user can close Quick View')
def close_quick_view(context):
    context.app.home_page.close_quick_view()


@then('Verify that user can see images')
def quick_view_click_images(context):
    context.app.home_page.quick_view_click_images()

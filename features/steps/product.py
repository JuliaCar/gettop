from behave import given, when, then


@given('Open GetTop product {product_id} page')
def open_product_page(context, product_id):
    context.app.page.open_page(product_id)


@then('Verify that every product has name, price, description')
def product_name_price_description(context):
    context.app.product_page.product_name_price_description()


@then('Verify that user can zoom in product image')
def soom_in_image(context):
    context.app.product_page.zoom_in_image()


@then('Verify that user can scroll thru images and close them')
def scroll_zoom_images(context):
    context.app.product_page.scroll_zoom_images()
    context.app.product_page.close_zoom_images()


@then('Click "Home" link')
def click_home_link(context):
    context.app.product_page.click_home_link()

@then('Verify that link takes to Home page')
def verify_home_page(context):
    context.app.home_page.vefiry_home_page()


@then('Verify that {category} category link takes to correct category page')
def click_category_link(context, category):
    context.app.product_page.click_category_link()
    context.app.product_page.open_correct_category_page(category)


# @then('Verify that {social_icons} logos are present')
# def logos_present(context, social_icons):
#     context.app.product_page.logos_present(social_icons)


@when('Hover over product image')
def hover_over_product_image(context):
    context.app.product_page.hover_over_product_image()


@then('Verify that user can click on the heart icon')
def click_heart_icon(context):
    context.app.product_page.click_heart_icon()



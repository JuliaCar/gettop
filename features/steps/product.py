from behave import given, when, then


@given('Open GetTop product {product_id} page')
def open_product_page(context, product_id):
    context.app.page.open_page(product_id)


@then('Verify that every product has name, price, description')
def product_name_price_description(context):
    context.app.product_page.product_name_price_description()


@then('Verify that user can zoom in product image')
def zoom_in_image(context):
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


@then('Verify that {social_icons} logos are present')
def logos_present(context, social_icons):
    context.app.logos_page.logos_present_facebook(social_icons)
    context.app.logos_page.logos_present_twitter(social_icons)
    context.app.logos_page.logos_present_email(social_icons)
    context.app.logos_page.logos_present_pinterest(social_icons)
    context.app.logos_page.logos_present_linkedin(social_icons)


@then('Verify that {logos_icons} logos are present in the loop')
def logos_present(context, logos_icons):
    context.app.logos_page.loop_logos_present(logos_icons)


@when('Click and switch to a new window with FACEBOOK page')
def fb_click_switch_new_window(context):
    context.app.logos_page.fb_click_switch_new_window()

@when('Click and switch to a new window with Twitter page')
def tw_click_switch_new_window(context):
    context.app.logos_page.tw_click_switch_new_window()

@when('Click and switch to a new window with Email page')
def email_click_switch_new_window(context):
    context.app.logos_page.email_click_switch_new_window()

@when('Click and switch to a new window with Pinterest page')
def pinterst_click_switch_new_window(context):
    context.app.logos_page.pinterest_click_switch_new_window()

@when('Click and switch to a new window with LinkedIn page')
def linkedin_click_switch_new_window(context):
    context.app.logos_page.linkedin_click_switch_new_window()

@then('A user can close new window and go to the original one')
def switch_old_window(context):
    context.app.logos_page.switch_old_window()

@then('Verify that {links} opens new window')
def social_links_opens(context, links):
    context.app.logos_page.social_links_opens(links)


@when('Hover over product image')
def hover_over_product_image(context):
    context.app.product_page.hover_over_product_image()


@then('Verify that user can click on the heart icon')
def click_heart_icon(context):
    context.app.product_page.click_heart_icon()

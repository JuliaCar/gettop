from behave import when, then

@then('User can click on "Home" link')
def click_home_link(context):
    context.app.shop_page.click_home_link()


@when('User can move left knot to the right to 50%')
def move_left_knot_right(context):
    context.app.shop_page.move_left_knot_right()

@when('User can move right knot to the left to 50%')
def ove_right_knot_left(context):
    context.app.shop_page.move_right_knot_left()

@when('User can click FILTER button')
def click_filter_btn(context):
    context.app.shop_page.click_filter_btn()

@then('Verify than filter was applied - {product_name} is shown')
def filter_applied_high_end(context, product_name):
    context.app.shop_page.filter_applied_high_end(product_name)

@then('Verify that user can reset filters')
def reset_filters(context):
    context.app.shop_page.reset_filters()

@when('User can move left knot to the right to 100%')
def move_left_knob_right_max(context):
    context.app.shop_page.move_left_knob_right_max()

@then('Verify that {msg_no_match} text are shown')
def message_no_product_shown(context, msg_no_match):
    context.app.shop_page.message_no_product_shown(msg_no_match)

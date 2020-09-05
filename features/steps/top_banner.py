from behave import then


@then('Can click left dot')
def banner_left_dot(context):
    context.app.home_page.banner_left_dot()


@then('Can click right dot')
def banner_right_dot(context):
    context.app.home_page.banner_right_dot()


@then('Can click left arrow')
def banner_left_arrow(context):
    context.app.home_page.banner_left_arrow()


@then('Can click right arrow')
def banner_right_arrow(context):
    context.app.home_page.banner_right_arrow()


@then('Can click on the banner')
def banner_click(context):
    context.app.home_page.banner_click()


@then('Verify that it taken to correct category page')
def correct_category_page(context):
    context.app.home_page.correct_category_page()

from behave import then


@then('Click on GetTop Logo')
def logo_click(context):
    context.app.top_nav_menu_page.logo_click()

from behave import then


@then('Verify click on Account icon opens {login_form} form')
def account_icon_login_form(context, login_form):
    context.app.top_nav_menu_page.account_icon_login_form(login_form)

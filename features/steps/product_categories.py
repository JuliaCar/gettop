from behave import then


@then('User hover over {number_categories} categories and see correct categories on menu options')
def hover_over_categories_top_menu(context, number_categories):
    context.app.top_nav_menu_page.hover_over_categories_topmenu(number_categories)


@then('Verify user can hover over {category_name} category')
def hover_over_category(context, category_name):
    context.app.top_nav_menu_page.hover_over_category(category_name)


@then('Verify user can see correct menu options')
def department_menu_options(context):
    context.app.top_nav_menu_page.department_menu_options()


@then('Verify user can click on MAC category')
def click_mac_category(context):
    context.app.top_nav_menu_page.click_mac_category()


@then('Verify user can click on IPHONE category')
def click_iphone_category(context):
    context.app.top_nav_menu_page.click_iphone_category()


@then('Verify user can click on IPAD category')
def click_ipad_category(context):
    context.app.top_nav_menu_page.click_ipad_category()


@then('Verify user can click on WATCH category')
def click_watch_category(context):
    context.app.top_nav_menu_page.click_watch_category()


@then('Verify user can click on ACCESSORIES category')
def click_accessories_category(context):
    context.app.top_nav_menu_page.click_accessories_category()


@then('Verify correct {category_name} category page opens')
def correct_category_page_opens(context, category_name):
    context.app.product_page.open_correct_category_page(category_name)

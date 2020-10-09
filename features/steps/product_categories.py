from behave import then


@then('User hover over {number_categories} categories and see correct categories on menu options')
def hover_over_categories_top_menu(context, number_categories):
    context.app.top_nav_menu_page.hover_over_categories_topmenu(number_categories)

@then('Verify user can hover over MAC category')
def hover_over_category_mac(context):
    context.app.top_nav_menu_page.hover_over_category_mac()


@then('Verify user can hover over IPHONE category')
def hover_over_category_iphone(context):
    context.app.top_nav_menu_page.hover_over_category_iphone()


@then('Verify user can hover over IPAD category')
def hover_over_category_ipad(context):
    context.app.top_nav_menu_page.hover_over_category_ipad()


@then('Verify user can hover over WATCH category')
def hover_over_category_watch(context):
    context.app.top_nav_menu_page.hover_over_category_watch()


@then('Verify user can hover over Accessories category')
def hover_over_category_accessories(context):
    context.app.top_nav_menu_page.hover_over_category_accessories()


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


@then('Verify user can see MAC correct menu options {menu_options}')
def correct_menu_options_mac(context, menu_options):
    context.app.product_page.correct_menu_options_mac(menu_options)


@then('Verify user can see IPHONE correct menu options {menu_options}')
def correct_menu_options_ipone(context, menu_options):
    context.app.product_page.correct_menu_options_iphone(menu_options)


@then('Verify user can see IPAD correct menu options {menu_options}')
def correct_menu_options_ipad(context, menu_options):
    context.app.product_page.correct_menu_options_ipad(menu_options)


@then('Verify user can see WATCH correct menu options {menu_options}')
def correct_menu_options_watch(context, menu_options):
    context.app.product_page.correct_menu_options_watch(menu_options)


@then('Verify user can see Accessories correct menu options {menu_options}')
def correct_menu_options_accessories(context, menu_options):
    context.app.product_page.correct_menu_options_accessories(menu_options)

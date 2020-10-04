from behave import given, when, then

@when('User move to checkout page')
def move_driver_checkout_page(context):
    context.app.checkout_page.move_driver_checkout_page()

@then('Verify that user can fill out checkout form')
def fillout_checkout_form(context):
    context.app.checkout_page.fillout_checkout_form()

@when('User can fill out first name {first_name}')
def fillout_first_name(context, first_name):
    context.app.checkout_page.fillout_first_name(first_name)

@when('User can fill out last name {last_name}')
def fillout_last_name(context, last_name):
    context.app.checkout_page.fillout_last_name(last_name)

@when('User can fill out company name {company_name}')
def fillout_company_name(context, company_name):
    context.app.checkout_page.fillout_company_name(company_name)

@when('User can fill out street {billing_address_1} and unit {billing_address_2}')
def fillout_street_address(context, billing_address_1, billing_address_2):
    context.app.checkout_page.fillout_street_address(billing_address_1, billing_address_2)

@when('User can fill out city {city}')
def fillout_city(context, city):
    context.app.checkout_page.fillout_city(city)

@when('User can fill out postcode {postcode}')
def fillout_postcode(context, postcode):
    context.app.checkout_page.fillout_postcode(postcode)

@when('User can fill out phone # {phone}')
def fillout_phone(context, phone):
    context.app.checkout_page.fillout_phone(phone)

@when('User can fill out email {email}')
def fillout_phone(context, email):
    context.app.checkout_page.fillout_email(email)

@when('User can choose country {country}')
def fillout_country(context, country):
    context.app.checkout_page.fillout_country(country)

@when('Click PLACE ORDER button')
def click_place_order_btn(context):
    context.app.checkout_page.click_place_order_btn()

@then('Verify that user can see message {message_required_field} is a required field')
def see_required_field_msg(context, message_required_field):
    context.app.checkout_page.see_required_field_msg(message_required_field)

@then('Verify user can go back to Cart by clicking {shopping_cart_header} icon')
def click_shopping_cart_icon(context, shopping_cart_header):
    context.app.top_nav_menu_page.shopping_cart_icon_click()
    context.app.checkout_page.verify_header_shopping_cart(shopping_cart_header)

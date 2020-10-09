from behave import given, when, then

@then('Verify user clicks number {page_number} page')
def click_page_number(context, page_number):
    context.app.shop_page.click_page_number(page_number)

@then('Verify it takes to {header_page_number} of shop')
def verify_page_number_header(context, header_page_number):
    context.app.shop_page.verify_page_number_header(header_page_number)

@then('Verify click trough multiple product pages by clicking {arrow} sign')
def verify_arrow_click(context, arrow):
    context.app.shop_page.verify_arrow_click(arrow)

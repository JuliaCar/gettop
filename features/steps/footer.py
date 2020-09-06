from behave import then


@then('Verify {footer_categories_list} categories are shown')
def footer_categories_shown(context, footer_categories_list):
    context.app.footer_page.footer_catefories_shown(footer_categories_list)


@then('Verify {copyright_text} sign shown in footer')
def footer_copyright_text(context, copyright_text):
    context.app.footer_page.footer_copyright_text(copyright_text)


@then('Verify go back to top button takes to top')
def back_top_btn(context):
    context.app.footer_page.footer_back_top_btn()


@then('Verify that every product has name, price, image and star-rating')
def footer_products_tags(context):
    context.app.footer_page.footer_products_tags()


@then('Verify footer has working links for all product categories')
def footer_links_categories(context):
    context.app.footer_page.footer_links_categories()

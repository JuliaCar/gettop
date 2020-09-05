from behave import then


@then('Verify text {categories_text_shown} is shown')
def categories_text_is_shown(context, categories_text_shown):
    context.app.home_page.categories_text_shown(categories_text_shown)


@then('Verify that correct categories are shown')
def correct_categories_shown(context):
    context.app.home_page.correct_categories_shown()


@then('Verify that upon clicking on each category, correct page opens')
def correct_page_opens(context):
    context.app.home_page.correct_page_opens()

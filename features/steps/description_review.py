from behave import given, when, then

@then('Verify that description block is shown')
def description_block_shown(context):
    context.app.description_review_page.description_block_shown()

@when('User can open review block')
def open_review_block(context):
    context.app.description_review_page.open_review_block()

@then('Verify that user can submit a {header_review}')
def user_submit_review(context, header_review):
    context.app.description_review_page.user_submit_review(header_review)

@then('Verify that review submitted')
def review_submitted(context):
    context.app.description_review_page.review_submitted()

@then('Verify that {amount_reviews} for {product_name} are shown')
def correct_amount_reviews(context, amount_reviews, product_name):
    context.app.description_review_page.correct_amount_reviews(amount_reviews, product_name)

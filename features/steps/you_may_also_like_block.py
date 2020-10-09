from behave import when, then


@then('Verify that {block_header} header block shown')
def you_may_also_like_text_shown(context, block_header):
    context.app.product_page.you_may_also_like_text_shown(block_header)

@then('Verify that block "You may also like.." contains products')
def block_contains_products(context):
    context.app.product_page.you_block_contains_products()

@then('Verify in "You may.." block {product_name} link is clickable, takes to correct pages')
def you_click_product1_take_correct_page(context, product_name):
    context.app.product_page.you_click_product1_take_correct_page(product_name)

@then('Verify "You may.." block {product_name} link is clickable and takes to correct pages')
def you_click_product2_take_correct_page(context, product_name):
    context.app.product_page.you_click_product2_take_correct_page(product_name)

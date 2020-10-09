from behave import when, then


@when('Add to wishlist by clicking on Heart icon')
def wishlist_click_icon(context):
    context.app.wishlist_page.click_heart_icon()


@then('Move to the wishlist page')
def move_wishlist_page(context):
    context.app.wishlist_page.click_heart_icon()


@then('Verify that user can see {product}')
def user_see_correct_product_name(context, product):
    context.app.wishlist_page.user_see_correct_product_name(product)


@when('Open another product page')
def another_product_page(context):
    context.app.wishlist_page.another_product_page()


@then('Verify user can see {amount_logos} social logos')
def wishlist_social_logos_present(context, amount_logos):
    context.app.wishlist_page.wishlist_social_logos_present(amount_logos)


@then('Delete item from wishlist')
def delete_item_wishlist(context):
    context.app.wishlist_page.delete_item_wishlist()


@then('Verify {no_item_wishlist} is shown')
def no_item_wishlist_text(context, no_item_wishlist):
    context.app.wishlist_page.no_item_wishlist_text(no_item_wishlist)

@then('User sees {msg_product_removed} message')
def wishlist_successfully_removed_msg(context, msg_product_removed):
    context.app.wishlist_page.wishlist_successfully_removed_msg(msg_product_removed)

@then('User click on wishlist item')
def wishlist_click_item(context):
    context.app.wishlist_page.wishlist_click_item()

@then('Verify it takes to correct product page')
def wishlist_correct_product_page(context):
    context.app.wishlist_page.wishlist_correct_product_page()

from behave import then, when


@then('Verify user can see {block_header} block header')
def browse_block_header_present(context, block_header):
    context.app.shop_page.browse_block_header_present(block_header)

@then('Verify user sees {categories} categories')
def browse_block_categories_shown(context, categories):
    context.app.shop_page.browse_block_categories_shown(categories)

@then('Verify user can click on MacBook category under Browse')
def browse_category_click_macbook(context):
    context.app.shop_page.browse_category_click_macbook()

@then('Verify it takes user {category} page')
def browse_category_correct_page(context, category):
    context.app.shop_page.browse_category_correct_page(category)

@then('Verify user can click on iPhone category under Browse')
def browse_category_click_iphone(context):
    context.app.shop_page.browse_category_click_iphone()

@then('Verify user can click on iPad category under Browse')
def browse_category_click_ipad(context):
    context.app.shop_page.browse_category_click_ipad()

@then('Verify user can click on Accessories category under Browse')
def browse_category_click_accessories(context):
    context.app.shop_page.browse_category_click_accessories()

@then('Verify user can click on AirPods category under Browse')
def browse_category_click_airpods(context):
    context.app.shop_page.browse_category_click_airpods()

@then('Verify user can click on Watch category under Browse')
def browse_category_click_watch(context):
    context.app.shop_page.browse_category_click_watch()

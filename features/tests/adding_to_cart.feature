# Created by julia cardenas at 9/6/20
Feature: Test Scenarios for Adding to cart feature

  Scenario: User can add product to cart
    Given Open GetTop product iphone-11pro page
    When Click on ADD TO CART button
    Then Verify that item added to the shopping cart

  Scenario: User can click - and + to modify amount of items to add to cart,
  upon adding to cart, correct amount of items shown in the cart
    Given Open GetTop product macbook-pro-16 page
    When Click + button 5 times
    When Click - button 3 times
    When Click on ADD TO CART button
    Then Verify that 3 items in cart
    #1 item is always present 1+5-3=3

  Scenario: User can type in amount of items to add to cart,
  upon adding to cart, correct amount of items shown in the cart
    Given Open GetTop product ipad page
    When User can type in 6 amount of items to add to cart
    When Click on ADD TO CART button
    Then Verify that 6 items in cart

  Scenario: User sees " ... have been added to your cart" confirmation upon adding items to cart
    Given Open GetTop product iphone-11pro page
    When Click on ADD TO CART button
    Then Verify user sees "...have been added to your cart" message confirmation

  Scenario: User can click through multiple product images by clicking back and forward arrows
    Given Open GetTop product airpods-pro page
    Then Verify user can click right arrow
    Then Verify user can click left arrow
    ### TODO add amount of click, for example: ('Verify user can click right arrow 5 times)
    ### TODO maybe try to write this TC in the for loop

  Scenario: If product is out of stock, user sees 'Out of Stock',
   Add to Cart and Checkout buttons are not shown (https://gettop.us/product/land-tee-jack-jones/)
    Given Open GetTop product land-tee-jack-jones page
    Then Verify user sees Out of stock message

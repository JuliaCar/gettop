# Created by julia cardenas at 9/6/20
Feature: Test Scenarios for Adding to cart feature

  Background:
  Given Open GetTop product iphone-11pro page

  Scenario: User can add product to cart
    When Click on ADD TO CART button
    Then Verify that item added to the shopping cart

  Scenario: User can click - and + to modify amount of items to add to cart,
  upon adding to cart, correct amount of items shown in the cart
    When Click + button 5 times
    When Click - button 3 times
    When Click on ADD TO CART button
    Then Verify that 3 items in cart

  Scenario: User can type in amount of items to add to cart,
  upon adding to cart, correct amount of items shown in the cart
    When User can type in 6 amount of items to add to cart
    When Click on ADD TO CART button
    Then Verify that 6 items in cart

  Scenario: User sees " ... have been added to your cart" confirmation upon adding items to cart
    When Click on ADD TO CART button
    Then Verify user sees "...have been added to your cart" message confirmation

Scenario: User can click through multiple products by clicking back and forward arrows

Feature: Test Scenarios for Adding to cart feature for product that out of stock
  Scenario: If product is out of stock, user sees 'Out of Stock',
   Add to Cart and Checkout buttons are not shown (https://gettop.us/product/land-tee-jack-jones/)
    Given Open GetTop product land-tee-jack-jones page
    Then Verify user sees Out of stock message
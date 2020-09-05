# Created by julia cardenas at 8/26/20
Feature: Test Scenarios for GetTop shopping cart on top nav menu

  Scenario: User clicks on Cart icon - opens Empty Cart page if no products were added
      Given Open GetTop home page
      When Click on the shopping cart icon
      Then Page contains Your cart is currently empty. are shown

  Scenario: User hover over empty cart icon shows "No products in the cart." message
    Given Open GetTop home page
    When Hover over the shopping cart icon
    Then Message No products in the cart. are shown

  Scenario: User add product and verify that price in top nav menu is correct
    Given Open product macbook-pro-13 page
    When Click on ADD TO CART button
    Then Verify that price in top nav menu cart is correct
         ####     not sure that it is correct

  Scenario: User add products, verify that amount of items shown in top nav menu are correct
    Given Open product airpods-pro page
    When Click on ADD TO CART button
    And User open other product page
    And Click on ADD TO CART button
    Then Verify that 2 items in cart

  ##5 have to think how to do it with loop Didn't verify 2nd product!!!
  Scenario: User add products to cart and verify correct products and subtotal shown
    Given Open product airpods-pro page
    When Click on ADD TO CART button
    And User open other product page
    And Click on ADD TO CART button
    Then Verify AirPods Pro and iPhone 11 Pro in the cart
    Then Verify that $1,248.00 price shown
  ##5 have to think how to do it with loop Didn't verify 2nd product!!!

  Scenario: User add products to cart and click on "View Cart" takes to cart page
    Given Open product macbook-air page
    When Click on ADD TO CART button
    And User open other product page
    When Click on ADD TO CART button
    Then Verify can click on View Cart
    And It takes to SHOPPING CART page


  Scenario: User add products to cart and verify click on "Checkout" on top menu - takes to checkout page
    Given Open product ipad-mini page
    When Click on ADD TO CART button
    And User open other product page
    When Click on ADD TO CART button
    Then  Verify that user can click on "Checkout" button
    And It takes to CHECKOUT DETAILS page

  Scenario: User add a product to cart, hover over cart icon, verify user can remove a product
    Given Open product ss-crew-california-sub-river-island page
    When Click on ADD TO CART button
    And Hover over the shopping cart icon
    Then User can remove product

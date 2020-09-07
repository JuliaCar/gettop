# Created by julia cardenas at 8/29/20
Feature: Test Scenarios for Latest on Sale

  Background:
    Given open GetTop home page

 Scenario: "Latest Products on Sale" text is shown
    Then Verify LATEST PRODUCTS ON SALE text is shown

  Scenario: Every product has Sale icon, image, product category, name, price, and star-rating
    When Verify that every product has all icons

  Scenario: User can click on heart icon to add to wishlist
    Then Verify user can click on heart icon

   Scenario: User can open product from Sale and add it to cart
    When Open product from Sale
    And Click on ADD TO CART button

  Scenario: User can open product from Sale and see product price and description
    When Open product from Sale
    Then Verify that user can see price and description

  Scenario: User can open and close Quick View by clicking on closing X
    Then Verify that user can open Quick View
    And Verify that user can close Quick View

  Scenario: User can click Quick View and add product to cart
    Then Verify that user can open Quick View
    When Click on ADD TO CART button

  Scenario: User can click Quick View and click through product images
    Then Verify that user can open Quick View
    And Verify that user can see images

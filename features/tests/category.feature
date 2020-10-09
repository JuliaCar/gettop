# Created by julia cardenas at 9/16/20
Feature: Test Scenarios for GetTop product categories

  Background:
    Given Open GetTop iphone category page

  Scenario: Only items of correct category are shown
   Then Verify items of iphone category are shown

  Scenario: "Showing all <N> results" is present and reflects correct amount of items (count amount of products on the page to verify this)
   Then Verify Showing all 3 results is present
   Then Verify that 3 items are present

  Scenario: All items have Category, Name and Price
    Then Verify that all items have Category, Name and Price

  Scenario: User can open and close Quick View by clicking on closing X
    Then Verify user can open Quick View
    And Verify that user can close Quick View

  Scenario: User can click Quick View and add product to cart
    Then Verify user can open Quick View
    And User can add products to cart in Quick View
    And Verify user sees "...have been added to your cart" message confirmation

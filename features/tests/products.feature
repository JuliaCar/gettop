# Created by julia cardenas at 9/17/20
Feature: Test Scenarios for Products feature

  Background:
    Given Open GetTop shop page

  Scenario: User can open and close Quick View by clicking on closing X
    Then Verify that user can open Quick View
    Then Verify that user can close Quick View

  Scenario: User can click Quick View and add product to cart
    Then Verify that user can open Quick View
    Then User can add products to cart in Quick View

  Scenario: User can click trough multiple product pages by clicking 1, 2 for page number
    Then Verify user clicks number 2 page
    And Verify it takes to PAGE 2 of shop
    Then Verify user clicks number 1 page
    And Verify it takes to HOME / SHOP of shop

  Scenario: User can click trough multiple product pages by clicking > and <
    Then Verify click trough multiple product pages by clicking > sign
    And Verify it takes to PAGE 2 of shop
    Then Verify click trough multiple product pages by clicking < sign
    And Verify it takes to HOME / SHOP of shop

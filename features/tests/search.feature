# Created by julia cardenas at 8/31/20
Feature: Test Scenarios for search bar on the top menu

  Scenario: User can search for existing product and sees correct results
    Given Open GetTop home page
    When Search for iPad mini product
    Then Verify user see iPad mini product page

  Scenario: User can search for non-existing product and see "No products were found matching your selection."
    Given Open GetTop home page
    When Search for Dress product
    Then Verify user see No products were found matching your selection. on page

# Created by julia cardenas at 9/18/20
Feature: Test Scenario for filter feature

  Background:
    Given Open GetTop shop page

  Scenario: "Home" link takes user to Home Page
    Then User can click on "Home" link
    And Verify LATEST PRODUCTS ON SALE text is shown

  Scenario: User can filter products by price
    When User can move left knot to the right to 50%
    And User can click FILTER button
    Then Verify than filter was applied - MacBook Pro 16-inch is shown

  Scenario: User can filter products by price
    When User can move right knot to the left to 50%
    And User can click FILTER button
    Then Verify than filter was applied - AirPods Pro is shown

  Scenario: User can reset price filter after they were applied
    When User can move right knot to the left to 50%
    And User can click FILTER button
    Then Verify that user can reset filters

  Scenario: "No products were found matching your selection." message shown if no products match selected filters
    When User can move left knot to the right to 100%
    And User can click FILTER button
    Then Verify that No products were found matching your selection. text are shown

# Created by julia cardenas at 9/15/20
Feature: Test Scenario for Description block on Product page

  Scenario Outline: Description block is shown
    Given Open GetTop product <item> page
    Then Verify that description block is shown

    Examples:
      |  item |
      | macbook-pro-13                      |
      | ss-crew-california-sub-river-island |
      | ipad-mini                           |
      | iphone-11pro                        |
      | airpods-pro                         |

  Scenario: User can submit a review
    Given Open GetTop product macbook-pro-16 page
    When User can open review block
    Then Verify that user can submit a review
    And Verify that review submitted

  Scenario:Correct amount of product reviews are shown
    Given Open GetTop product iphone-se page
    When User can open review block
    Then Verify that REVIEWS (1) for iPhone SE are shown

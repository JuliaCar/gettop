# Created by julia cardenas at 9/2/20
Feature: Test Scenario for Footer

  Background:
    Given open GetTop home page

  Scenario: Footer shows Best Selling, Latest, Top Rated categories
    Then Verify BEST SELLING, LATEST, TOP RATED categories are shown

  Scenario:"Copyright 2020" shown in footer
    Then Verify Copyright 2020 © Gettop sign shown in footer

  Scenario: Footer has button to go back to top
    Then Verify go back to top button takes to top

  Scenario: All products in the footer have name, price, image and star-rating
    Then Verify that every product has name, price, image and star-rating
      ###TODO Bug! there is no rating in latest category iPhone11

  Scenario: Footer has working links to all product categories
    Then Verify footer has working links to all product categories

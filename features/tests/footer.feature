# Created by julia cardenas at 9/2/20
Feature: Test Scenario for Footer

  Scenario: Footer shows Best Selling, Latest, Top Rated categories
    Given Open GetTop home page
    Then Verify BEST SELLING, LATEST, TOP RATED categories are shown

  Scenario:"Copyright 2020" shown in footer
    Given Open GetTop home page
    Then Verify Copyright 2020 © Gettop sign shown in footer

  Scenario: Footer has button to go back to top
    Given Open GetTop home page
    Then Verify go back to top button takes to top

  Scenario: All products in the footer have name, price, image and star-rating
    Given Open GetTop home page
    Then Verify that every product has name, price, image and star-rating
      ###did not verify star-rating!!!

  Scenario: Footer has working links to all product categories
    Given Open GetTop home page
    Then Verify footer has working links for all product categories

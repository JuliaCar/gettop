# Created by julia cardenas at 8/30/20
Feature: Test Scenarios for Browse Categories

  Scenario: "Browse Our Categories" text is shown
    Given Open GetTop home page
    Then Verify text BROWSE OUR CATEGORIES is shown

  Scenario: 4 correct categories are shown
    Given Open GetTop home page
    Then Verify that correct categories are shown

  Scenario: Upon clicking on each category, correct page opens
    Given Open GetTop home page
    Then Verify that upon clicking on each category, correct page opens

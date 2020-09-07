# Created by julia cardenas at 8/30/20
Feature: Test Scenarios for Browse Categories

  Background:
    Given open GetTop home page

  Scenario: "Browse Our Categories" text is shown
    Then Verify text BROWSE OUR CATEGORIES is shown

  Scenario: 4 correct categories are shown
    Then Verify that correct categories are shown

  Scenario: Upon clicking on each category, correct page opens
    Then Verify that upon clicking on each category, correct page opens

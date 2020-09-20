## Created by juliacardenas at 8/31/20
Feature: Test Scenarios for top navigation menu - product categories

  Background:
    Given open GetTop home page

  Scenario: User can hover over categories and see correct menu options
    Then User hover over 5 categories and see correct categories on menu options

  Scenario: User can select Mac product from top menu and correct page opens
    Then Verify user can click on MAC category
    And Verify correct MACBOOK category page opens

  Scenario: User can select iPhone product from top menu and correct page opens
    Then Verify user can click on IPHONE category
    And Verify correct IPHONE category page opens

  Scenario: User can select iPad product from top menu and correct page opens
    Then Verify user can click on IPAD category
    And Verify correct IPAD category page opens

  Scenario: User can select Watch product from top menu and correct page opens
    Then Verify user can click on WATCH category
    And Verify correct WATCH category page opens

  Scenario: User can select Accessories product from top menu and correct page opens
    Given Open GetTop home page
    Then Verify user can click on ACCESSORIES category
    And Verify correct ACCESSORIES category page opens

    ### TODO Didn't do it, don't know how to verify "can see correct menu options"??
##  Scenario: User can hover over Mac and see correct menu options
##    Given Open GetTop home page
##    Then Verify user can hover over MAC category
##    And Verify user can see correct menu options
##
##  Scenario: User can hover over iPad and see correct menu options
##  Scenario: User can hover over Watch and see correct menu options
##  Scenario: User can hover over Accessories and see correct menu options
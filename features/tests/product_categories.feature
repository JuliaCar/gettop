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

  Scenario: User can hover over Mac and see correct menu options
    Then Verify user can hover over MAC category
    And Verify user can see MAC correct menu options MacBook Pro 13-inch, MacBook Pro 16-inch, MacBook Air

  Scenario: User can hover over IPHONE and see correct menu options
    Then Verify user can hover over IPHONE category
    And Verify user can see IPHONE correct menu options iPhone 11, iPhone 11 Pro, iPhone SE

  Scenario: User can hover over IPAD and see correct menu options
    Then Verify user can hover over IPAD category
    And Verify user can see IPAD correct menu options iPad, iPad Pro, iPad mini, iPad Air

  Scenario: User can hover over Watch and see correct menu options
    Then Verify user can hover over WATCH category
    And Verify user can see WATCH correct menu options Watch Series 5, Watch Series 3

  Scenario: User can hover over Accessories and see correct menu options
    Then Verify user can hover over Accessories category
    And Verify user can see Accessories correct menu options AirPods with Wireless Charging Case, AirPods Pro

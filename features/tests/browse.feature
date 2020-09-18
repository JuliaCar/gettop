# Created by juliacardenas at 9/17/20
Feature:  Test Scenarios for

  Background:
    Given Open GetTop shop page

#  Scenario: User sees correct categories under Browse
#    Then Verify user can see BROWSE block header
#    Then Verify user sees Accessories, AirPods, Watches, iPad, iPhone, MacBook categories

  Scenario: User sees click on MacBook category under Browse and correct page opens
    Then Verify user can click on MacBook category under Browse
    Then Verify it takes user MacBook page

  Scenario: User sees click on iPhone category under Browse and correct page opens
    Then Verify user can click on iPhone category under Browse
    Then Verify it takes user iPhone page

  Scenario: User sees click on iPad category under Browse and correct page opens
    Then Verify user can click on iPad category under Browse
    Then Verify it takes user iPad page

  Scenario: User sees click on Accessories category under Browse and correct page opens
    Then Verify user can click on Accessories category under Browse
    Then Verify it takes user Accessories page

  Scenario: User sees click on AirPods category under Browse and correct page opens
    Then Verify user can click on AirPods category under Browse
    Then Verify it takes user AirPods page

  Scenario: User sees click on Watch category under Browse and correct page opens
    Then Verify user can click on Watch category under Browse
    Then Verify it takes user Watch page


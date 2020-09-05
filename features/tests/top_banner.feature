# Created by julia cardenas at 8/29/20
Feature: Test Scenario for top banner

  Scenario: User can click right and left arrows to see top banners
    Given Open GetTop home page
    Then Can click right arrow
    And Can click left arrow

  Scenario: User can click bottom dots to see top banners
    Given Open GetTop home page
    Then Can click right dot
    And Can click left dot

  Scenario: User can click on product banner and is taken to correct category page
    Given Open GetTop home page
    Then Can click on the banner
    And Verify that it taken to correct category page
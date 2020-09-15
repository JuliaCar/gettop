# Created by juliacardenas at 9/7/20
Feature: Test Scenario for "You may also like…" block

  Scenario: "You may also like…" bock is shown
    Given Open GetTop product iphone-se page
    Then Verify that You may also like… header block shown

  Scenario: "You may also like…" bock contains products
    Given Open GetTop product airpods-pro page
    Then Verify that block "You may also like.." contains products

  Scenario: Product links under "You may also like…" block are clickable and take to correct pages
    Given Open GetTop product iphone-11pro page
    Then Verify in "You may.." block iPhone SE link is clickable, takes to correct pages

  Scenario: Product links under "You may also like…" block are clickable and take to correct pages
    Given Open GetTop product iphone-11pro page
    Then Verify "You may.." block iPhone 11 link is clickable and takes to correct pages

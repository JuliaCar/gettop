# Created by julia cardenas at 9/19/20
Feature: Test Scenarios for Wishlist feature

  Background:
    Given Open GetTop product macbook-pro-16 page
    When Add to wishlist by clicking on Heart icon
#    When Move to another product page
#    Then Move to the wishlist page


  Scenario:Add product to wishlist, verify user sees correct products
    Then Verify that user can see macbook-pro-16

#Add products to wishlist, verify user can remove product and sees a confirmation message
#Add products to wishlist, verify user can click on wishlist item and is taken to correct product page
#User can see social logos to share wishlist items
#
#
#    "No products added to the wishlist'" shown if no product were added to the list
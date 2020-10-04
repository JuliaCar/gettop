# Created by julia cardenas at 9/19/20
Feature: Test Scenarios for Wishlist feature

  Background:
    Given Open GetTop product macbook-pro-16 page
    When Add to wishlist by clicking on Heart icon

#  Scenario: Add product to wishlist, verify user sees correct products
#    Then Move to the wishlist page
#    Then Verify that user can see MacBook Pro 16-inch
#
#  Scenario: "No products added to the wishlist" shown if no product were added to the list
#   Then Move to the wishlist page
#   Then Delete item from wishlist
#   Then Verify No products added to the wishlist is shown
#
#  Scenario: User can see social logos to share wishlist items
#    Then Move to the wishlist page
#    Then Verify user can see 4 social logos
#
 ###TODO cann't add second product to the wishlist #StaleElement :(
  Scenario: Add products to wishlist, verify user can remove product and sees a confirmation message
    When Open another product page
    When Add to wishlist by clicking on Heart icon
    Then Move to the wishlist page
    Then Delete item from wishlist
    Then User sees Product successfully removed. message

  Scenario: Add products to wishlist, verify user can click on wishlist item and is taken to correct product page
    When Open another product page
    When Add to wishlist by clicking on Heart icon
    Then Move to the wishlist page
    Then User click on wishlist item
#    Then Verify it takes to correct product page






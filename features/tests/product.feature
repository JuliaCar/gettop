# Created by julia cardenas at 9/4/20
Feature: Test Scenarios for Product page

  Scenario: Product has image, name, price, description
    Given Open GetTop product macbook-pro-13 page
    Then Verify that every product has name, price, description

  Scenario: User can zoom in product image, scroll thru images and close them (by clicking X)
   Given Open GetTop product iphone-se page
   Then Verify that user can zoom in product image
   And Verify that user can scroll thru images and close them

  Scenario: User can add product to wishlist by hovering over product image and clicking on the heart icon
    Given Open GetTop product ipad-mini page
    When Hover over product image
    Then Verify that user can click on the heart icon

  Scenario: Category link takes users to correct category page
    Given Open GetTop product airpods page
    Then Verify that ACCESSORIES category link takes to correct category page

  Scenario: "Home" link takes user to Home Page
    Given Open GetTop product ipad-air page
    Then Click "Home" link
    Then Verify that link takes to Home page

#  Scenario: Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn
#    Given Open GetTop product macbook-air page
##    Then Verify that Facebook, Twitter, Email, Pinterest, LinkedIn logos are present
#         ###### Didn't verify !!!

#  Scenario: Clicking on a social network link opens a new window to login to social network
#    Given Open GetTop product macbook-air page
#    ######Then Verify social network links opens a new window to login to social network
      ###### Didn't verify !!!
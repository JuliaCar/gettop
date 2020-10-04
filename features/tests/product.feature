# Created by julia cardenas at 9/4/20
Feature: Test Scenarios for Product page

  Scenario Outline: Product has image, name, price, description
    Given Open GetTop product <item> page
    Then Verify that every product has name, price, description
    Examples:
      |  item |
      | macbook-pro-13                      |
      | ss-crew-california-sub-river-island |
      | ipad-mini                           |
      | iphone-11pro                        |
      | airpods-pro                         |

  Scenario: User can zoom in product image, scroll thru images and close them (by clicking X)
    Given Open GetTop product macbook-pro-13 page
    Then Verify that user can zoom in product image
    And Verify that user can scroll thru images and close them

  Scenario: User can add product to wishlist by hovering over product image and clicking on the heart icon
    Given Open GetTop product macbook-pro-16 page
    When Hover over product image
    Then Verify that user can click on the heart icon

  Scenario: Category link takes users to correct category page
    Given Open GetTop product macbook-air page
    Then Verify that MACBOOK category link takes to correct category page

  Scenario: "Home" link takes user to Home Page
    Given Open GetTop product iphone-11 page
    Then Click "Home" link
    Then Verify that link takes to Home page

  Scenario: Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn
    Given Open GetTop product iphone-11pro page
    Then Verify that Facebook, Twitter, Email, Pinterest, Tumblr logos are present

  Scenario: Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn in the LOOP "for"
    Given Open GetTop product iphone-se page
    Then Verify that Facebook, Twitter, Email, Pinterest, Tumblr logos are present in the loop

  Scenario: Clicking on a Facebook link opens a new window to login to social network
    Given Open GetTop product ipad page
    When Click and switch to a new window with FACEBOOK page
    Then A user can close new window and go to the original one

  Scenario: Clicking on a Twitter link opens a new window to login to social network
    Given Open GetTop product ipad-pro page
    When Click and switch to a new window with Twitter page
    Then A user can close new window and go to the original one

  Scenario: Clicking on a Email link opens a new window to login to social network
    Given Open GetTop product ipad-mini page
    When Click and switch to a new window with EMAIL page
    Then A user can close new window and go to the original one

  Scenario: Clicking on a Pinterest link opens a new window to login to social network
    Given Open GetTop product ipad-air page
    When Click and switch to a new window with Pinterest page
    Then A user can close new window and go to the original one

  Scenario: Clicking on a LinkedIn link opens a new window to login to social network
    Given Open GetTop product ss-crew-california-sub-river-island page
    When Click and switch to a new window with Tumblr page
    Then A user can close new window and go to the original one

 ##TODO try to do a loop for open the social pages
 # TODO Lna - how verify email?? why doesn't work and how to verify

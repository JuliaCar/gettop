# Created by julia cardenas at 9/18/20
Feature: Test Scenarios for Checkout feature

  Background:
    Given Open product macbook-pro-13 page
    When Click on ADD TO CART button
    When User move to checkout page

  Scenario: User can fill out checkout form
    When User can fill out first name John
    When User can fill out last name Doe
    When User can fill out company name FlyingFish
    When User can fill out street 3910 Middlefield Rd and unit Apt 3
    When User can fill out city Palo Alto
    When User can fill out postcode 94303
    When User can fill out phone # 9876543210
    When User can fill out email test@gmail.com
    When Click PLACE ORDER button

  Scenario: User cannot leave any required fields blank (no first name)
    When User can fill out last name Doe
    When User can fill out company name FlyingFish
    When User can fill out street 3910 Middlefield Rd and unit Apt 3
    When User can fill out city Palo Alto
    When User can fill out postcode 94303
    When User can fill out phone # 9876543210
    When User can fill out email test@gmail.com
    When Click PLACE ORDER button
    Then Verify that user can see message Billing First name is a required field

  Scenario: User cannot leave any required fields blank (no last name)
    When User can fill out first name John
    When User can fill out company name FlyingFish
    When User can fill out street 3910 Middlefield Rd and unit Apt 3
    When User can fill out city Palo Alto
    When User can fill out postcode 94303
    When User can fill out phone # 9876543210
    When User can fill out email test@gmail.com
    When Click PLACE ORDER button
    Then Verify that user can see message Billing Last name is a required field

  Scenario: User cannot leave any required fields blank (no street)
    When User can fill out first name John
    When User can fill out last name Doe
    When User can fill out company name FlyingFish
    When User can fill out city Palo Alto
    When User can fill out postcode 94303
    When User can fill out phone # 9876543210
    When User can fill out email test@gmail.com
    When Click PLACE ORDER button
    Then Verify that user can see message Billing Street address is a required field

   Scenario: User cannot leave any required fields blank (no city)
    When User can fill out first name John
    When User can fill out last name Doe
    When User can fill out company name FlyingFish
    When User can fill out street 3910 Middlefield Rd and unit Apt 3
    When User can fill out postcode 94303
    When User can fill out phone # 9876543210
    When User can fill out email test@gmail.com
    When Click PLACE ORDER button
    Then Verify that user can see message Billing Town / City is a required field

   Scenario: User cannot leave any required fields blank (no phone)
    When User can fill out first name John
    When User can fill out last name Doe
    When User can fill out company name FlyingFish
    When User can fill out street 3910 Middlefield Rd and unit Apt 3
    When User can fill out city Palo Alto
    When User can fill out postcode 94303
    When User can fill out email test@gmail.com
    When Click PLACE ORDER button
    Then Verify that user can see message Billing Phone is a required field

  Scenario: User cannot leave any required fields blank (no email)
    When User can fill out first name John
    When User can fill out last name Doe
    When User can fill out company name FlyingFish
    When User can fill out street 3910 Middlefield Rd and unit Apt 3
    When User can fill out city Palo Alto
    When User can fill out postcode 94303
    When User can fill out phone # 9876543210
    When Click PLACE ORDER button
    Then Verify that user can see message Billing Email address is a required field

  Scenario: User can go back to Cart by clicking 'Shopping Cart'
    Then Verify user can go back to Cart by clicking Shopping Cart icon


#  Scenario: User can select any country from country, state drop down
#    ######When User can choose country United States, state
  #TODO was able to do it with select ??

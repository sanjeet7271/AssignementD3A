Feature: D3A Home Page and Login Functionality
  Scenario: Login to D3A Home Page
    Given Launch the browser
    When Open D3A homepage
    And Click on Login button from D3A homepage
    And Enter username "sanjeet.aot@gmail.com" and password "qaz123123"
    And Click on login button
    Then verify that the logged in successfully

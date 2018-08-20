Feature: Login
  In order to use the app the user must be able to Login

  Scenario: Login Success
    Given the user has the correct credentials
    When the user enters username
    When the user enters password
    And clicks Login
    Then the user is presented with a welcome message


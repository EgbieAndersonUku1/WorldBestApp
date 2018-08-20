Feature: Attempt to logging in with invalid credentials


  Scenario Outline: trying to log in user with <username> and <password> credentials
      Given we have a user
      When the user enters the "<username>" username
      And the user enters the "<password>" password
      And user clicks Login
      Then user is presented with a error message

      Examples:
            | username                       | password             |
            | incorrect_username@email.com   | incorrect_password   |
            | incorrect_username@email.com   | supers3cret          |
            | test@drugdev.com               | incorrect_password   |






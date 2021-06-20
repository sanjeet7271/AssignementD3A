Feature: Create new Project in D3A

  Background: common Steps for login functionality
    Given Launch the browser
    When Open D3A homepage
    And Click on Login button from D3A homepage
    And Enter username "sanjeet.aot@gmail.com" and password "qaz123123"
    And Click on login button

    Scenario Outline: Create new project and validate created successful
        When project "<Project_Name>" is already exits then delete it
        And Click on Projects
        Then Click on New Project
        And Enter Project Name "<Project_Name>" and Project Description "<Project_Description>"
        Then Add the Project
        Then Verify Project "<Project_Name>" added successfully
        Examples:
          | Project_Name | Project_Description |
          | Project_D3A  | demo test           |

    Scenario Outline: Create new simulation under project and validate created successful
        When verify project "<Project_Name>" is created
        Then Click on expand button to expand created project
        And verify if simulation is already is created then delete it
        Then Click on New Simulation button
        And Click on plus icon to add first node
        And Click on Project icon from left panel
        Then Verify default simulation is added into project
        Examples:
          | Project_Name |
          | Project_D3A  |
          | demo    |

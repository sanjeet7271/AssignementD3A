# Python selenium BDD Framework

## Features supported
1. Functional UI Automation by using Selenium
2. Reading Global Url from Properties file
3. Test cases by Gherkins BDD framework

## Pre-requisite
1. Python 
2. pyCharm

## plugins required to installed into pyCharm
1. pip install selenium
2. pip install behave
3. pip install allure-behave

## How to Run 
1. Please clone git project ot required location
2. import project into PyCharm
3. Go to `Features\`
4. Go to `Configuration\Config.ini` and Change browser name to Chrome/Firefox to run test case on required browser
5. Run command: `behave Features\`
6. Run command for allure report: `behave -f allure_behave.formatter:AllureFormatter -o reports/ Features/`

	
## To view Report 
1. Go to the Screenshots `\Screenshots` to check failed test cases
2. Go to Reports '\Reports' to check allure repors

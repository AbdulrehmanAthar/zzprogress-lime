Feature:As a user, I want to be able to create an account on Oodo.com so that I can access all of its features.
Scenario: User successfully creates an account with valid credentials
Given I am on the Oodo.com sign-up page
When I enter valid credentials
And click the "Create Account" button
Then I should be redirected to the dashboard
And my account should be created successfully

Scenario: User enters an invalid email address while creating an account
Given I am on the Oodo.com sign-up page
When I enter an invalid email address
And valid credentials for other fields
And click the "Create Account" button
Then I should see an error message that the email address is invalid

Scenario: User enters an existing email address while creating an account
Given I am on the Oodo.com sign-up page
When I enter an email address that is already associated with an existing account
And valid credentials for other fields
And click the "Create Account" button
Then I should see an error message that the email address already exists

Scenario: User creates an account with a weak password
Given I am on the Oodo.com sign-up page
When I enter weak password credentials
And valid credentials for other fields
And click the "Create Account" button
Then I should see an error message that the password is weak

Scenario: User enters an invalid phone number while creating an account
Given I am on the Oodo.com sign-up page
When I enter an invalid phone number
And valid credentials for other fields
And click the "Create Account" button
Then I should see an error message that the phone number is invalid

Scenario: User leaves a required field blank while creating an account
Given I am on the Oodo.com sign-up page
When I leave a required field blank
And click the "Create Account" button
Then I should see an error message that the field is required

Scenario: User successfully creates an account with all optional fields filled
Given I am on the Oodo.com sign-up page
When I enter valid credentials for all optional fields
And click the "Create Account" button
Then I should be redirected to the dashboard
And my account should be created successfully

Scenario: User navigates away from the sign-up page without completing the form
Given I am on the Oodo.com sign-up page
When I click on a link or button that navigates me away from the page
Then I should be prompted with a warning message that my progress will be lost

Scenario: User navigates to the sign-up page while already logged in
Given I am logged in to my Oodo.com account
When I navigate to the sign-up page
Then I should be redirected to the dashboard
And see a message that I am already logged in

Scenario: User creates an account with long and complex credentials
Given I am on the Oodo.com sign-up page
When I enter long and complex credentials
And click the "Create Account" button
Then I should be redirected to the dashboard
And my account should be created successfully
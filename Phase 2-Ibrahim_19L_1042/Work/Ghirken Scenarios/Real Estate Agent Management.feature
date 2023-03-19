Feature: Real Estate Agent Management

Scenario: Agent manages their listings
    Given the real estate agent has logged in to their account
    When they navigate to the manage listings section
    And they add a new property to the active listings category
    Then the new property should be visible in the active listings category

Scenario: Agent tracks leads for an active listing
    Given the real estate agent has logged in to their account
    And they have an active listing with leads
    When they navigate to the track leads section for that listing
    Then they should see a list of leads for that listing

Scenario: Agent tracks commissions for a sold listing
    Given the real estate agent has logged in to their account
    And they have a sold listing with commissions
    When they navigate to the track commissions section for that listing
    Then they should see a list of commissions for that listing

Scenario: Agent generates a report for active listings
    Given the real estate agent has logged in to their account
    And they have active listings in their account
    When they navigate to the generate reports section
    And they select the active listings category
    Then a report should be generated for the active listings

Scenario: Agent generates a report for inactive listings
    Given the real estate agent has logged in to their account
    And they have inactive listings in their account
    When they navigate to the generate reports section
    And they select the inactive listings category
    Then a report should be generated for the inactive listings

Scenario: Agent generates a report for sold listings
    Given the real estate agent has logged in to their account
    And they have sold listings in their account
    When they navigate to the generate reports section
    And they select the sold listings category
    Then a report should be generated for the sold listings

Scenario: Agent adds a new property to active listings
    Given the real estate agent has logged in to their account
    And they navigate to the manage listings section
    And they select the active listings category
    When they add a new property to the category
    Then the new property should be visible in the active listings category

Scenario: Agent updates an existing property in active listings
    Given the real estate agent has logged in to their account
    And they navigate to the manage listings section
    And they select an existing property in the active listings category
    When they update the property details
    Then the changes should be saved and visible in the active listings category

Scenario: Agent adds a lead to an active listing
    Given the real estate agent has logged in to their account
    And they have an active listing with no leads
    When they navigate to the track leads section for that listing
    And they add a lead to the listing
    Then the lead should be visible in the list of leads for that listing

Scenario: Agent adds a commission to a sold listing
    Given the real estate agent has logged in to their account
    And they have a sold listing with no commissions
    When they navigate to the track commissions section for that listing
    And they add a commission to the listing
    Then the commission should be visible in the list of commissions for that listing
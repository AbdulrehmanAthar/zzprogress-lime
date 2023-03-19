Feature: Financial Advisor Portfolio Management

  As a financial advisor,
  I want to be able to manage my clients' portfolios,
  track performance, and generate reports,
  so that I can provide better financial advice and grow my business.

  Scenario: Generate performance report for active client
    Given an active client with positive portfolio performance
    When the financial advisor generates a performance report
    Then the report should be generated successfully

  Scenario: Review portfolio for active client with negative performance
    Given an active client with negative portfolio performance
    When the financial advisor reviews the portfolio
    Then the advisor should advise changes to improve the portfolio

  Scenario: Generate final report for closed client
    Given a closed client
    When the financial advisor generates a final report
    Then the report should be generated successfully

  Scenario: Unable to generate report for inactive client
    Given an inactive client
    When the financial advisor attempts to generate a report
    Then the report should not be generated

  Scenario: Unable to generate report for client with zero balance
    Given a client with a portfolio balance of $0
    When the financial advisor attempts to generate a report
    Then the report should not be generated

  Scenario: Unable to generate report for client with negative balance
    Given a client with a portfolio balance of -$1
    When the financial advisor attempts to generate a report
    Then the report should not be generated

  Scenario: Unable to generate more than 100 reports
    Given a request to generate 101 reports
    When the financial advisor attempts to generate the reports
    Then the reports should not be generated

  Scenario: Generate multiple reports for active client
    Given an active client with positive portfolio performance
    When the financial advisor generates 10 reports
    Then 10 reports should be generated successfully

  Scenario: Unable to generate report for client with balance over $1,000,000,000
    Given a client with a portfolio balance of $1,000,000,001
    When the financial advisor attempts to generate a report
    Then the report should not be generated

  Scenario: Unable to generate report for client with performance over 100%
    Given a client with a portfolio performance of 101%
    When the financial advisor attempts to generate a report
    Then the report should not be generated
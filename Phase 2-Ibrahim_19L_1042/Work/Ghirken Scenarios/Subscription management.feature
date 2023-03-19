Feature: Subscription Management
As a small business owner with a subscription-based model, I want to be able to manage my subscriptions, track revenue and churn, and generate reports, so that I can optimize my subscription business and improve customer retention.

Scenario 1: Create Subscription
Given a customer has selected a subscription plan
When the customer completes the subscription creation process
Then the subscription is created in the system
And the customer is notified of successful subscription creation

Scenario 2: Update Subscription
Given a customer has an existing subscription
When the customer updates the subscription plan
Then the subscription plan is updated in the system
And the customer is notified of successful subscription update

Scenario 3: Cancel Subscription
Given a customer has an existing subscription
When the customer cancels the subscription
Then the subscription is cancelled in the system
And the customer is notified of successful subscription cancellation

Scenario 4: Track Revenue
Given a customer has an existing subscription
When the customer generates a revenue report
Then the system generates a revenue report for the customer's subscription
And the revenue report is sent to the customer

Scenario 5: Track Churn Rate
Given a customer has an existing subscription
When the customer tracks the churn rate
Then the system calculates and displays the churn rate for the customer's subscription

Scenario 6: Track Retention Rate
Given a customer has an existing subscription
When the customer tracks the retention rate
Then the system calculates and displays the retention rate for the customer's subscription

Scenario 7: Generate Monthly Report
Given a customer has an existing subscription
When the customer generates a monthly report
Then the system generates a report summarizing subscription activity for the past month
And the report is sent to the customer

Scenario 8: Generate Quarterly Report
Given a customer has an existing subscription
When the customer generates a quarterly report
Then the system generates a report summarizing subscription activity for the past quarter
And the report is sent to the customer

Scenario 9: Generate Annual Report
Given a customer has an existing subscription
When the customer generates an annual report
Then the system generates a report summarizing subscription activity for the past year
And the report is sent to the customer

Scenario 10: Handle Invalid Subscription Type
Given a customer selects an invalid subscription type
When the customer completes the subscription creation process
Then the system displays an error message indicating an invalid subscription type
And the subscription is not created in the system
Feature: As a freelancer, I want to be able to easily create and send invoices to my clients, so that I can get paid quickly and efficiently. Odo.com's invoicing feature would make this process much easier for me.
Scenario: Creating a new invoice
Given I am logged in to my Odo.com account
When I click on the "Create Invoice" button
And I fill out the necessary details, such as client name, invoice date, and payment terms
And I add the items I am invoicing for, including their descriptions and prices
Then the invoice is created successfully and I can view it in my invoice list.

Scenario: Editing an existing invoice
Given I am logged in to my Odo.com account
And I have an existing invoice that I need to edit
When I navigate to the invoice and click the "Edit" button
And I make the necessary changes to the invoice details or items
Then the invoice is updated successfully and the changes are saved.

Scenario: Deleting an invoice
Given I am logged in to my Odo.com account
And I have an existing invoice that I need to delete
When I navigate to the invoice and click the "Delete" button
Then the invoice is deleted successfully and is no longer visible in my invoice list.

Scenario: Sending an invoice to a client
Given I am logged in to my Odo.com account
And I have an existing invoice that I need to send to a client
When I navigate to the invoice and click the "Send" button
And I enter the client's email address and any additional notes
Then the invoice is sent successfully to the client's email address.

Scenario: Generating a PDF version of an invoice
Given I am logged in to my Odo.com account
And I have an existing invoice that I need to generate a PDF for
When I navigate to the invoice and click the "Generate PDF" button
Then a PDF version of the invoice is downloaded or displayed on the screen.

Scenario: Adding a discount to an invoice
Given I am logged in to my Odo.com account
And I have an existing invoice that I need to add a discount to
When I navigate to the invoice and click the "Add Discount" button
And I enter the discount amount or percentage
Then the discount is applied successfully to the invoice and the total is updated.

Scenario: Viewing payment history for an invoice
Given I am logged in to my Odo.com account
And I have an existing invoice that has been paid
When I navigate to the invoice and click the "View Payment History" button
Then I can see a record of all payments made for the invoice, including the date, amount, and payment method.

Scenario: Setting up recurring invoices
Given I am logged in to my Odo.com account
And I need to create recurring invoices for a client
When I navigate to the client's profile and click the "Recurring Invoices" button
And I set up the necessary details, such as invoice frequency and start date
Then the recurring invoices are set up successfully and will be generated automatically according to the schedule.

Scenario: Accepting payments online
Given I am logged in to my Odo.com account
And I have an existing invoice that a client wants to pay online
When I navigate to the invoice and click the "Accept Online Payment" button
And the client enters their payment information and submits the payment
Then the payment is processed successfully and the invoice is marked as paid.

Scenario: Generating a report of unpaid invoices
Given I am logged in to my Odo.com account
And I need to generate a report of all unpaid invoices
When I navigate to the "Reports"




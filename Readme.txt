Unit Testing & API Testing Framework

There are multiple framework present for Unit and Api testing but the one which we selected for our project are as follows:

1)Jest

Jest is primarily a testing framework for JavaScript projects and doesn't have native support for 
Selenium testing. However, you can still use Jest with Selenium WebDriver to write automated tests for web applications.
 Here's an example of how to use Jest and Selenium WebDriver to test a web application:

**API Test File Example**

The test file for the Selenium WebDriver tests should be named `test.js`. 
Here's an example of a test file for automating a login flow using Selenium WebDriver and Jest:

```javascript
const { Builder, By, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const chromedriver = require('chromedriver');

chrome.setDefaultService(new chrome.ServiceBuilder(chromedriver.path).build());

describe('Login flow', () => {
  let driver;

  beforeAll(async () => {
    driver = await new Builder().forBrowser('chrome').build();
  });

  afterAll(async () => {
    await driver.quit();
  });

  it('should login successfully', async () => {
    await driver.get('https://example.com/login');
    await driver.findElement(By.name('username')).sendKeys('testuser');
    await driver.findElement(By.name('password')).sendKeys('testpassword');
    await driver.findElement(By.tagName('form')).submit();
    await driver.wait(until.titleIs('Dashboard'), 5000);
    expect(await driver.getCurrentUrl()).toEqual('https://example.com/dashboard');
  });
});
```

In the API test file example, we are using Jest to write automated tests for a web application. 
The tests are written using the Selenium WebDriver API, which allows us to automate interactions with a web browser. Here's a breakdown of the code:

1. `require` statements: We use `require` statements to import the necessary dependencies for our tests. 
We import `Builder`, `By`, and `until` from the `selenium-webdriver` package, which provides the core API
 for interacting with a web browser. We also import `chrome` and `chromedriver` to configure and start the Chrome browser.

2. `describe` block: We use the `describe` function to group our tests together. In this case, we group all the tests related to the login flow.

3. `beforeAll` and `afterAll` hooks: These hooks are run before and after all the tests in the `describe` block.
 In this example, we use the `beforeAll` hook to create a new Chrome driver instance and the `afterAll`
 hook to close the driver instance.

4. Test case: We use the `it` function to define a test case. In this example, we define a test case that
 navigates to a login page, enters a username and password, submits the form, and then asserts that the user is redirected to the dashboard page. We use the `expect` function to perform the assertion.

5. Selenium WebDriver API: Within the test case, we use the Selenium WebDriver API to interact with 
the web page. For example, we use `driver.get` to navigate to the login page, `driver.findElement` to find form elements, `sendKeys` to enter text into the form, and `submit` to submit the form.

6. Assertion: We use Jest's `expect` function to make an assertion about the current URL of the page.
 If the assertion fails, Jest will report an error.



**Unit Test File Example**

For unit testing, you can write test files with the naming convention `*.test.js`. Here's an example of a unit test file for a function that calculates the sum of two numbers:

```javascript
function sum(a, b) {
  return a + b;
}

describe('sum', () => {
  it('calculates the sum of two numbers', () => {
    expect(sum(1, 2)).toBe(3);
    expect(sum(2, 2)).toBe(4);
    expect(sum(-1, 1)).toBe(0);
  });
});
```

In the unit test file example, we are using Jest to write unit tests for a JavaScript function. Here's a breakdown of the code:

1. `describe` block: We use the `describe` function to group our tests together. 
In this case, we group all the tests related to the `sum` function.

2. Test case: We use the `it` function to define a test case. In this example, 
we define a test case that checks that the `sum` function returns the expected result for different inputs.

3. Assertion: We use Jest's `expect` function to make an assertion about the output of the `sum` function.
 If the assertion fails, Jest will report an error.

In both examples, Jest provides a simple and intuitive API for writing tests.
 It allows us to group tests together using `describe` and `it`, and provides built-in assertion functions like `expect` for making assertions about our code. With Jest, we can easily write and run automated tests for both API and unit testing.


I hope this example helps illustrate how to use Jest with Selenium WebDriver 
for API and unit testing in a JavaScript project.


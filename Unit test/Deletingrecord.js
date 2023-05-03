 const { Builder, By } = require('selenium-webdriver');
import jest from 'jest';
const chrome = require('selenium-webdriver/chrome');
const path = require('path');

describe('Odoo unit tests', () => {
  let driver;

  beforeAll(async () => {
    // Set the path to the chromedriver executable
    const chromedriverPath = path.join(__dirname, '..', 'E:\My downloads\chromedriver_win32 (1)', 'chromedriver.exe');

    // Start the ChromeDriver service
    const service = new chrome.ServiceBuilder(chromedriverPath).build();
    chrome.setDefaultService(service);

    // Create webdriver instance with path to ChromeDriver
    driver = await new Builder().forBrowser('chrome').build();
  });

  afterAll(async () => {
    await driver.quit();
  });

 describe('Deleting a record', () => {
    test('should delete an existing partner record', async () => {
      // Navigate to the Odoo login page
      await driver.get('http://localhost:8069/web/login');

      // Log in to Odoo
      await driver.findElement(By.name('login')).sendKeys('admin');
      await driver.findElement(By.name('password')).sendKeys('admin');
      await driver.findElement(By.css('button[type=submit]')).click();

      // Navigate to the partners page
      await driver.get('http://localhost:8069/web#menu_id=115&action=129');

      // Click on the first partner in the list to delete it
      await driver.findElement(By.css('.o_list_view tbody tr:first-child td.o_list_record_selector input')).click();

      // Click on the delete button to delete the selected partner record
      await driver.findElement(By.css('.o_list_button_remove')).click();

      // Confirm the deletion
      await driver.findElement(By.css('.o_confirm_buttons .btn-primary')).click();

      // Assert that the partner record was deleted successfully
      const partners = await driver.findElements(By.css('.o_list_view tbody tr'));
      expect(partners).toHaveLength(0);
    });
  });
});
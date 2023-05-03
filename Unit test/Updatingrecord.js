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

describe('Updating a record', () => {
    test('should update an existing partner record', async () => {
      // Navigate to the Odoo login page
      await driver.get('http://localhost:8069/web/login');

      // Log in to Odoo
      await driver.findElement(By.name('login')).sendKeys('admin');
      await driver.findElement(By.name('password')).sendKeys('admin');
      await driver.findElement(By.css('button[type=submit]')).click();

      // Navigate to the partners page
      await driver.get('http://localhost:8069/web#menu_id=115&action=129');

      // Click on the first partner in the list to edit it
      await driver.findElement(By.css('.o_list_view tbody tr:first-child td.o_data_cell:first-child')).click();

      // Update the name of the partner
      await driver.findElement(By.css('.o_field_char[name="name"] input')).clear();
      await driver.findElement(By.css('.o_field_char[name="name"] input')).sendKeys('Updated Partner');

      // Save the updated partner record
      await driver.findElement(By.css('.o_form_button_save')).click();

      // Assert that the partner record was updated successfully
      const partnerName = await driver.findElement(By.css('.o_form_view .o_field_char[name="name"]')).getText();
           expect(partnerName).toBe('Updated Partner');
    });
  });
  });
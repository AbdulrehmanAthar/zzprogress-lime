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

  describe('Creating a new record', () => {
    test('should create a new partner record', async () => {
      // Navigate to the Odoo login page
      await driver.get('http://localhost:8069/web/login');

      // Log in to Odoo
      await driver.findElement(By.name('login')).sendKeys('admin');
      await driver.findElement(By.name('password')).sendKeys('admin');
      await driver.findElement(By.css('button[type=submit]')).click();

      // Navigate to the partners page
      await driver.get('http://localhost:8069/web#menu_id=115&action=129');

      // Click on the create button to create a new partner record
      await driver.findElement(By.css('.o_list_button_add')).click();

      // Enter the name of the new partner record
      await driver.findElement(By.css('.o_field_char[name="name"] input')).sendKeys('Test Partner');

      // Save the new partner record
      await driver.findElement(By.css('.o_form_button_save')).click();

      // Assert that the new partner record was created successfully
      const partners = await driver.findElements(By.css('.o_list_view tbody tr'));
      expect(partners).toHaveLength(1);
      const partnerName = await partners[0].findElement(By.css('.o_data_cell:nth-child(2)')).getText();
      expect(partnerName).toBe('Test Partner');
    });
  });
  });
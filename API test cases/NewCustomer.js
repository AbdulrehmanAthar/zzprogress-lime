// Required libraries:
// npm install jest selenium-webdriver axios chromedriver
import jest from 'jest';
const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const { ServiceBuilder } = require('selenium-webdriver/chrome');
const axios = require('axios');

describe('API tests with Selenium', () => {
  let driver;
  let service;

  beforeAll(async () => {
    const chromedriverPath = 'E:\\My downloads\\chromedriver_win32 (1)\\chromedriver.exe';
    service = new ServiceBuilder(chromedriverPath).build();
    await service.start();
    driver = await new Builder()
      .forBrowser('chrome')
      .setChromeOptions(new chrome.Options().headless())
      .build();
  });

  afterAll(async () => {
    await driver.quit();
    await service.stop();
  });

  describe('Create a new customer', () => {
    test('should create a new customer and return 201 Created', async () => {
      await driver.get('https://odoo-api.example.com');
      const token = await driver.findElement(By.name('token')).getAttribute('value');

      const response = await axios.post('/api/v1/customers', {
        name: 'John Doe',
        email: 'johndoe@example.com',
        phone: '123-456-7890',
        address: '123 Main St',
      }, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      expect(response.status).toBe(201);

      const { data } = await axios.get(`/api/v1/customers/${response.data.id}`);

      expect(data.name).toBe('John Doe');
      expect(data.email).toBe('johndoe@example.com');
      expect(data.phone).toBe('123-456-7890');
      expect(data.address).toBe('123 Main St');
    });
  });
});
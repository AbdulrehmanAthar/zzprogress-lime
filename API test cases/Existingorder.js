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
 
 describe('Update an existing order', () => {
    test('should update an existing order and return 200 OK', async () => {
      await driver.get('https://odoo-api.example.com');
      const token = await driver.findElement(By.name('token')).getAttribute('value');

      const orderId = 123;
      const response = await axios.put(`/api/v1/orders/${orderId}`, {
        status: 'shipped',
        shippingAddress: '456 Secondary St',
        products: [
          { id: 456, quantity: 2 },
          { id: 789, quantity: 3 },
        ],
      }, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      expect(response.status).toBe(200);

      const { data } = await axios.get(`/api/v1/orders/${orderId}`);

      expect(data.status).toBe('shipped');
      expect(data.shippingAddress).toBe('456 Secondary St');
      expect(data.products).toContainEqual({ id: 456, quantity: 2 });
      expect(data.products).toContainEqual({ id: 789, quantity: 3 });
    });
  });

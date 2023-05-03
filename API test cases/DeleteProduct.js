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
  describe('Delete a product variant', () => {
    test('should delete a product variant and return 204 No Content', async () => {
      await driver.get('https://odoo-api.example.com');
      const token = await driver.findElement(By.name('token')).getAttribute('value');

      const productId = 456;
      const { data: variants } = await axios.get(`/api/v1/products/${productId}/variants`, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      expect(variants).not.toHaveLength(0);

      const variantIdToDelete = variants[0].id;

      const response = await axios.delete(`/api/v1/products/${productId}/variants/${variantIdToDelete}`, {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

    expect(response.status).toBe(204);

    try {
      await axios.get(`/api/v1/products/${productId}/variants/${variantIdToDelete}`);
    } catch (error) {
      expect(error.response.status).toBe(404);
    }
  });
});
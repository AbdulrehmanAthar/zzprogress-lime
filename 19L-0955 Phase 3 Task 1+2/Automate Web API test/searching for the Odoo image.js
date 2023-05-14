const { Builder } = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');
const request = require('requests');

describe('Docker Hub API', () => {
  let driver;

  beforeAll(async () => {
    driver = await new Builder()
      .forBrowser('firefox')
      .setFirefoxOptions(new firefox.Options().headless())
      .build();
  });

  afterAll(async () => {
    await driver.quit();
  });

  test('Search for the Odoo image', async () => {
    const query = 'odoo';
    const url = 'https://hub.docker.com/v2/search/repositories';
    const response = await request.get(url, { params: { query } });

    expect(response.status_code).toBe(200);

    const searchResults = response.json().results;
    const expectedImageName = 'odoo';
    expect(searchResults.some((result) => result.name.includes(expectedImageName))).toBe(true);

    const expectedImageVersion = 'latest';
    expect(searchResults.some((result) => result.name.includes(expectedImageVersion))).toBe(true);

    const expectedIsOfficial = true;
    expect(searchResults.some((result) => result.is_official === expectedIsOfficial)).toBe(true);
  });
});

import { test, expect } from '@playwright/test';


test.describe('Integration Test', () => {


  test('should display correct message from backend on frontend', async ({page}) => {

      // Wait for the frontend to load
      await page.goto('http://127.0.0.1:52012/',{waitUntil:'networkidle'});

      // Extract the message displayed on the frontend
      const message = await page.textContent('body > h1');

      // Log the message (optional)
      console.log('Message displayed on frontend:', message);


      const expectedMessageFromBackend = 'Hello from the Backend!';
      expect(message).toEqual(expectedMessageFromBackend);
  });
});

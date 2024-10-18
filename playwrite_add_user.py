import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch a browser
        browser = await p.chromium.launch(headless=False)  # Set headless=True to run without a GUI
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the login page
        await page.goto('https://test.deliverycentralplatform.ibm.com/digite/Request?Key=framework_main&ContainedURL=singleton_router&ItemType=EDPS_f&OwnerType=Prj&CFM=Y&ProjectId=51389&OwnerID=51389&uls=Y&SessionKey=Y&childProcessId=9bfKh5CFxZTyyDpobLIOJo9GCszTrl0fGYBvcK8B2WQ93D')

        # Fill in the username and password
        await page.fill('input[name="username"]', 'Pushkraj.kulkarni@ibm.com')
        await page.fill('input[name="password"]', 'your_password')

        # Click the login button
        await page.click('button[type="submit"]')

        # Wait for navigation to complete after logging in
        await page.wait_for_navigation()

        # Optionally, you can take a screenshot or do other actions
        await page.screenshot(path='screenshot.png')

        # Close the browser
        await browser.close()

# Run the async function
asyncio.run(run())

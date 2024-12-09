from playwright.sync_api import sync_playwright

def open_url_and_login(email):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Open the URL
        page.goto("https://test.deliverycentralplatform.ibm.com/digite")
        
        # Directly fill the email input field
        page.fill('input[type="email"]', email)
        
        # Click the "Continue" button
        page.click('button:has-text("Continue")')
        
        print("Entered email and clicked Continue")

        input("Press Enter to close the browser...")  # Keeps browser open until Enter is pressed

if __name__ == "__main__":
    open_url_and_login("your-email@example.com")  # Replace with the actual email ID

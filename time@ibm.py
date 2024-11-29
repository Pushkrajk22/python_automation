import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


# check the working for some weeks and then replace the save button with Submit

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://time.ibm.com/")
    page.goto("https://login.w3.ibm.com/saml/sps/auth")
    page.goto("https://login.w3.ibm.com/idaas/mtfim/sps/idaas/login?runtime=true&Target=https%3A%2F%2Flogin.w3.ibm.com%2Fsaml%2Fsps%2Fauth")
    page.get_by_role("button", name=" w3id Credentials  Use your").click()
    page.get_by_placeholder("IBM email address (e.g. jdoe@").click()
    page.get_by_placeholder("IBM email address (e.g. jdoe@").fill("Pushkraj.Kulkarni@ibm.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("")
    page.get_by_role("button", name="Sign in").click()
    page.goto("https://login.w3.ibm.com/saml/sps/auth?stateid=879fef84-0841-4647-9131-10b8ec813cd5")
    page.goto("https://time.ibm.com/login/callback?tkn=eyJhbGciOiJIUzUxMiJ9.eyJleHAiOjE3MzIyNTM4MDUsInRkIjp7InczIjoiUHVzaGtyYWouS3Vsa2FybmlAaWJtLmNvbSIsImNuIjoiMDA1Qk9PNzQ0IiwiZm4iOiJQdXNoa3JhaiBLdWxrYXJuaSIsImFkIjpmYWxzZSwib2MiOiJGUSIsImRlcHQiOiJKMTkiLCJockNvbXBhbnlDb2RlIjoiMDA2MyIsImVtcGxveWVlQ291bnRyeUNvZGUiOiI3NDQifX0.bCjRglzIZg27LNBocHuFFENxd_RwGcgt00ubvZ26_58R0lZ_jCtCrNuXKeZab4nEgrjke8hZcBYQxJCWRW67lQ&RelayState=7835df68-08ec-46d0-bfc9-b67c8b9b08e4")
    page.goto("https://time.ibm.com/login/callback")
    page.goto("https://time.ibm.com/week")
    page.locator("app-empty-grid-empty div").filter(has_text="Copy from a previous week").nth(4).click()
    page.get_by_role("combobox", name="Week ending").locator("div").nth(2).click()
    page.get_by_text("October 11,").click()
    page.get_by_role("button", name="Ok").click()
    page.locator(".ag-row-odd > div:nth-child(7) > .ng-star-inserted > .mat-tooltip-trigger").click()
    page.get_by_role("textbox").fill("9")
    page.locator(".ag-row-odd > div:nth-child(8) > .ng-star-inserted > .mat-tooltip-trigger").click()
    page.get_by_role("textbox").fill("9")
    page.locator(".ag-row-odd > div:nth-child(9) > .ng-star-inserted > .mat-tooltip-trigger").click()
    page.get_by_role("textbox").fill("9")
    page.locator(".ag-row-odd > div:nth-child(10) > .ng-star-inserted > .mat-tooltip-trigger").click()
    page.get_by_role("textbox").fill("9")
    page.locator(".ag-row-odd > div:nth-child(11) > .ng-star-inserted > .mat-tooltip-trigger").click()
    page.get_by_role("textbox").fill("9")
    #page.locator("div").filter(has_text="Week ending: November 22,").nth(1).click()


    page.get_by_role("button", name="Submit").click()
    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    try:
        run(playwright)
    except Exception as e:
        print("Below Error occured in the program. The data was not saved", e)

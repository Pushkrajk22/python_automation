import os
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    
    if True:

        page = context.new_page()
        page.goto("https://test.deliverycentralplatform.ibm.com/digite/")
        # page.goto("https://prepiam.ice.ibmcloud.com/oidc/sps/auth?client_id=YmNkOGY1YzEtOTc3YS00&Target=https%3A%2F%2Fprepiam.ice.ibmcloud.com%2Foidc%2Fendpoint%2Fdefault%2Fauthorize%3FqsId%3D0b65d8f9-c057-4334-b062-153cdde6fcf9%26client_id%3DYmNkOGY1YzEtOTc3YS00")
        # page.goto("https://prepiam.ice.ibmcloud.com/idaas/mtfim/sps/idaas/login?client_id=YmNkOGY1YzEtOTc3YS00&Target=https%3A%2F%2Fprepiam.ice.ibmcloud.com%2Foidc%2Fendpoint%2Fdefault%2Fauthorize%3FqsId%3D0b65d8f9-c057-4334-b062-153cdde6fcf9%26client_id%3DYmNkOGY1YzEtOTc3YS00")
        # page.goto("https://prepiam.ice.ibmcloud.com/authsvc/mtfim/sps/authsvc?PolicyId=urn:ibm:security:authentication:asf:basicldapuser&Target=https%3A%2F%2Fprepiam.ice.ibmcloud.com%2Foidc%2Fendpoint%2Fdefault%2Fauthorize%3FqsId%3D0b65d8f9-c057-4334-b062-153cdde6fcf9%26client_id%3DYmNkOGY1YzEtOTc3YS00")
        
        page.get_by_label("IBMid").fill("Pushkraj.kulkarni@ibm.com")
        page.get_by_role("button", name="Continue").click()
        page.get_by_role("button", name=" w3id Credentials  Use your").click()
        page.get_by_placeholder("IBM email address (e.g. jdoe@").fill("Pushkraj.kulkarni@ibm.com")
        page.get_by_placeholder("Password").fill("JaiGajanan$2002")
        page.locator("#showHidePw").click()
        page.get_by_role("button", name="Sign in").click()

        # Wait for successful login (you might want to add a wait condition for successful login)
        # page.wait_for_url("https://test.deliverycentralplatform.ibm.com/digite/Request?Key=check_password")
        
    print("Searching projects")
    # Proceed with other actions
    try:
        page.get_by_text("Recent Projects").click()
        page.locator("#projectIcon").get_by_role("list").get_by_text("View My Projects").click()
    except Exception as e:
        print("Exception in 1st try location recent projects")
        try:
            page.locator("#projectIcon").click()
            page.locator("#projectIcon").get_by_role("list").get_by_text("View My Projects").click()
        except Exception as e:
            print("Exception in 2nd try location recent projects")
            try:
                page.get_by_role("link", name="").click()
                page.locator("#projectIcon").get_by_role("list").get_by_text("View My Projects").click()
            except Exception as e:
                print("Exception in 3rd try location recent projects")
    
    time.sleep(10)
    try:
        page.locator("iframe[name=\"content\"]").get_by_text("Test Project_UT").click()
        print("Worked")
    except Exception as e:
        print("Exception in selecting the project")

    try:
        page.locator("iframe[name=\"content\"]").content_frame().get_by_text("More Multi Sort Print Column").click()
        page.locator("iframe[name=\"content\"]").content_frame().get_by_title("Other Accessible Projects").locator("span").first.click()
    except Exception as e:
        print("1st Exception in selecting more")
        try:
            page.get_by_text("More").click()
            page.get_by_text("Other Accessible Projects").click()
        except Exception as e:
            print("2nd Exception in selecting more")
            
    page.locator("#PROJECTNAME-triggerEl").click()
    page.get_by_role("menuitem", name="Filters ").click()
    page.get_by_placeholder(" ", exact=True).click()
    page.get_by_placeholder(" ", exact=True).fill("Test Project_UT")
    page.locator("#button-1706").click()

 


    page.get_by_text("Project Setup", exact=True).click()
    page.get_by_text("Additional Resources").click()
    page.get_by_role("button", name=" Add").click()
    page.locator("iframe[name=\"content\"]").content_frame().locator("[id=\"_Text_Check_CM_Name\"]").click()
    page.locator("iframe[name=\"content\"]").content_frame().locator("[id=\"_Text_Check_CM_Name\"]").fill("User Addition")
    page.locator("iframe[name=\"content\"]").content_frame().locator("[id=\"_Text_Check_CM_Name\"]").press("Enter")
    page.locator("iframe[name=\"content\"]").content_frame().get_by_role("cell", name="User Addition", exact=True).click(button="right")
    page.goto("https://test.deliverycentralplatform.ibm.com/digite/Request?Key=framework_main&ContainedURL=dyn_list&ItemType=RSRQ_f&OwnerType=Prj&CFM=Y&ProjectId=51282&OwnerID=51282&uls=Y&SessionKey=Y&childProcessId=YyesoOF1QiIIA3xWwj975eH4JEjc892BxyOTmn3282c92FM93D")
    page.locator("iframe[name=\"content\"]").content_frame().locator("iframe[name=\"eform_seg_393789\"]").content_frame().locator("[id=\"metric_comp_55963\\#88031\\#13485945\\#field1\"]").fill("import re\nfrom playwright.sync_api import Playwright, sync_playwright, expect\n\n\ndef run(playwright: Playwright) -> None:\n    browser = playwright.chromium.launch(headless=False)\n    context = browser.")
    page.locator("iframe[name=\"content\"]").content_frame().locator("iframe[name=\"eform_seg_393789\"]").content_frame().locator("[id=\"metric_comp_55963\\#88031\\#13485945\\#field5\"]").select_option("Project Manager")
    page.locator("iframe[name=\"content\"]").content_frame().locator("[id=\"_Text_Check_CM_Name\"]").fill("User Addition")
    page.locator("iframe[name=\"content\"]").content_frame().locator("iframe[name=\"eform_seg_393789\"]").content_frame().locator("[id=\"metric_comp_55963\\#88031\\#13485978\\#field1\"]").fill("debbie.buckle-CIC-UK@uk.ibm.com")
    page.locator("iframe[name=\"content\"]").content_frame().locator("iframe[name=\"eform_seg_393789\"]").content_frame().locator("[id=\"metric_comp_55963\\#88031\\#13485978\\#field5\"]").select_option("Project Manager")

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

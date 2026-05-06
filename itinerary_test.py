from playwright.sync_api import Playwright, sync_playwright, expect
import re


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # ---------------- LOGIN ----------------
    page.goto("https://kryptosportal-brgsgphsfng0edga.centralindia-01.azurewebsites.net/en/login")
    page.wait_for_timeout(3000)

    page.get_by_role("textbox", name="Employee code / Email").fill("KIT044")
    page.wait_for_timeout(3000)

    page.get_by_role("textbox", name="Password").fill("Madhu@123")
    page.wait_for_timeout(3000)

    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(3000)

    # Close popup if present
    try:
        page.get_by_role("button", name="close").click(timeout=3000)
    except:
        pass

    page.wait_for_timeout(3000)

    # ---------------- NAVIGATION ----------------
    page.get_by_role("link", name="Claims Portal").click()
    page.wait_for_timeout(3000)

    page.get_by_role("link", name="Travel Request & Claim").click()
    page.wait_for_timeout(3000)

    page.get_by_role("link", name="Itinerary Request").click()
    page.wait_for_timeout(3000)

    # ---------------- NEW ITINERARY ----------------
    page.get_by_role("button", name="New Itinerary").click()
    page.wait_for_timeout(3000)

    page.get_by_role("radio", name="Domestic").check()
    page.wait_for_timeout(3000)

    page.get_by_role("radio", name="One Way").check()
    page.wait_for_timeout(3000)

    # ---------------- JOURNEY ----------------
    page.get_by_role("textbox", name="Journey From *").fill("Chennai")
    page.wait_for_timeout(3000)

    page.get_by_role("textbox", name="Journey To *").fill("Salem")
    page.wait_for_timeout(3000)

    page.locator(".MuiInputAdornment-root").click()
    page.wait_for_timeout(3000)

    page.get_by_role("gridcell", name="6", exact=True).click()
    page.wait_for_timeout(3000)

    page.get_by_role("radio", name="Yes").check()
    page.wait_for_timeout(3000)

    # ---------------- AGENCY ----------------
    page.get_by_role("textbox", name="Agency Name *").fill("AVMS")
    page.wait_for_timeout(3000)

    page.get_by_role("textbox", name="Agency Phone Number *").fill("8779655918")
    page.wait_for_timeout(3000)

    # ---------------- CONTACT ----------------
    page.get_by_role("textbox", name="Alternative Contact Number (").fill("9751009076")
    page.wait_for_timeout(3000)

    page.get_by_role("textbox", name="Purpose of Travel *").fill("WORK")
    page.wait_for_timeout(3000)

    # ---------------- COUNTRY ----------------
    page.get_by_label("Select Country").click()
    page.wait_for_timeout(3000)

    page.get_by_role("textbox", name="Search").fill("India")
    page.wait_for_timeout(3000)

    page.get_by_text("India").click()
    page.wait_for_timeout(3000)

    # ---------------- AMOUNT ----------------
    page.get_by_role("spinbutton", name="Advance Amount").fill("20000")
    page.wait_for_timeout(3000)

    # ---------------- FILE UPLOAD ----------------
    page.set_input_files(
        "input[type='file']",
        r"C:\Users\madhumitha.a\hitayu\test\FILES\Shift_Assignment_Template_2026-04-24.xlsx"
    )

    # Wait for upload success
    page.wait_for_selector("text=File uploaded successfully")
    page.wait_for_timeout(3000)

    # ---------------- REMOVE BLOCKING NOTIFICATION ----------------
    page.evaluate("""
        const elements = document.querySelectorAll('[class*="MuiAlert"], [class*="notification"]');
        elements.forEach(el => el.remove());
    """)
    page.wait_for_timeout(3000)

    # ---------------- CLICK NEXT ----------------
    page.get_by_role("button", name="Next").click(force=True)
    page.wait_for_timeout(3000)

    # ---------------- VALIDATION ----------------
    expect(page).to_have_url(re.compile("itinerary", re.IGNORECASE))

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
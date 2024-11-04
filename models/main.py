from playwright.sync_api import expect
from datetime import datetime

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/"

    def navigate(self):
        self.page.goto(self.url, wait_until="load")
        expect(self.page).to_have_url(self.url+"#/login")
        expect(self.page.get_by_role("link", name="Robi").first).to_be_visible()
    
    def loginCreds(self):
        expect(self.page.get_by_role("heading", name="Login to Your Account")).to_be_visible()

        expect(self.page.get_by_placeholder("Enter User ID")).to_be_visible()
        self.page.get_by_placeholder("Enter User ID").click()
        self.page.get_by_placeholder("Enter User ID").fill("Nazia01")
        
        expect(self.page.get_by_placeholder("Password")).to_be_visible()
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill("Autumn@#923")
        
        expect(self.page.get_by_role("button", name="Sign In")).to_be_visible()
        self.page.get_by_role("button", name="Sign In").click()
        expect(self.page.get_by_text("Signed In Successfully.")).to_be_visible()
        self.page.get_by_label("close").click()

    def confirmSignIn(self):
        # expect(self.page.get_by_text("Signed In Successfully.")).to_be_visible()
        # self.page.get_by_label("close").click()
        expect(self.page.get_by_text("Welcome")).to_be_visible()
        expect(self.page.get_by_role("link", name="Dashboard")).to_be_visible()

class Dashboard():
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/dashboard"

    def findReport(self):
        expect(self.page.get_by_text("Reports", exact=True)).to_be_visible()
        self.page.get_by_text("Reports", exact=True).click()

    def findMasterDataReport(self):
        expect(self.page.get_by_text("Master Data Reports")).to_be_visible()
        self.page.get_by_text("Master Data Reports").click()

    def findDeviceReports(self):
        expect(self.page.get_by_text("Device Reports")).to_be_visible()
        self.page.get_by_text("Device Reports").click()
        
    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_text((self.title)+" Report")).to_be_visible()
        expect(self.page).to_have_url(self.url)

    def isDateFilled(self, today):
        expect(self.page.locator("input[name=\"fromDate\"]")).to_have_value(today)

    def enterDateFrom(self, month):
        expect(self.page.locator("input[name=\"fromDate\"]")).to_be_visible()
        self.page.locator("input[name=\"fromDate\"]").fill(month)

    def enterDateFromTo(self, today, month):
        expect(self.page.locator(self.datefromloc)).to_be_visible()
        self.page.locator(self.datefromloc).fill(month)
        expect(self.page.locator(self.datetoloc)).to_be_visible()
        self.page.locator(self.datetoloc).fill(today)

    def enterSecondDateFromTo(self, today, month):
        expect(self.page.locator(self.seconddatefrom)).to_be_visible()
        self.page.locator(self.seconddatefrom).fill(month)
        expect(self.page.locator(self.seconddateto)).to_be_visible()
        self.page.locator(self.seconddateto).fill(today)

    def viewReport(self):
        expect(self.page.get_by_role("button", name="View Report")).to_be_visible()
        self.page.get_by_role("button", name="View Report").click()

    def noDataFound(self):
        expect(self.page.get_by_text("No data found")).to_be_visible()

    def closeReport(self):
        self.page.get_by_text("×Close").click()
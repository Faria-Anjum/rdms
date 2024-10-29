from playwright.sync_api import expect
from models.main import Dashboard
from models.reports import ActivationDetails, SimActivationReport
#ActivationDetails for clickReport pointing to own name
#SimActivationReport for date fields fromDate toDate


class RCPendingDeviceOD(SimActivationReport):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/rc-pending-device-od-report"
        self.title = "RC Pending Device OD"

    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_text("RC Pending OD Device Report")).to_be_visible()

class PendingDeviceOD(SimActivationReport):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/pending-device-od-report"
        self.title = "Pending Device OD"

    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_text("Pending Device OD Device Report")).to_be_visible()

class FaultyDevice(SimActivationReport):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/faulty-device"
        self.title = "Faulty Device"

    def clickReport(self):
        return Dashboard.clickReport(self)
    
class DeviceTransaction(SimActivationReport):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/device-transaction"
        self.title = "Device Transaction"

    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title, exact=True)).to_be_visible()
        self.page.get_by_role("link", name=self.title, exact=True).click()
        expect(self.page.get_by_text((self.title)+" Report")).to_be_visible()
        expect(self.page).to_have_url(self.url)
    
class DeviceLifetimeTracking(SimActivationReport): #twoyears
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/device-life-time-tracking"
        self.title = "Device Life Time Tracking"

    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_text("Device Lifetime Tracking Report")).to_be_visible()

class DeviceRegistrationReport(SimActivationReport): #onemonth
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/device-registration"
        self.title = "Device Registration Report"


#     page.get_by_role("link", name="Device Life Time Tracking").click()
#     page.locator(".svg-inline--fa").first.click()
#     page.locator("input[name=\"fromDate\"]").fill("2024-08-29")
#     page.get_by_role("button", name="View Report").click()
#     page.locator("div").filter(has_text="No data found").nth(3).click()
#     page.locator("input[name=\"fromDate\"]").fill("2024-07-29")
#     page.get_by_role("button", name="View Report").click()
#     page.locator("input[name=\"fromDate\"]").fill("2022-07-29")
#     page.get_by_role("button", name="View Report").click()
#     page.get_by_text("×Close").click()
#     page.locator("nav").filter(has_text="nazianazia01Change").locator("svg").click()
#     page.get_by_role("link", name="Device Status").click()
#     page.locator("div").filter(has_text=re.compile(r"^Date RangeTo$")).first.click()
#     page.get_by_role("button", name="View Report").click()
#     page.locator("input[name=\"fromDate\"]").fill("2024-08-29")
#     page.get_by_role("button", name="View Report").click()
#     page.locator("input[name=\"fromDate\"]").fill("2022-08-29")
#     page.get_by_role("button", name="View Report").click()
#     page.get_by_text("×Close").click()
#     page.locator("nav").filter(has_text="nazianazia01Change").locator("svg").click()
#     page.get_by_role("link", name="Central Inventory Stock").click()
#     page.locator("path").first.click()
#     page.get_by_text("×Close").click()
#     page.locator(".svg-inline--fa").first.click()
#     page.get_by_role("button", name="View Report").click()
#     page.get_by_text("×Close").click()
#     page.locator("input[name=\"regFromDate\"]").fill("2024-08-29")
#     page.locator("input[name=\"regToDate\"]").fill("2024-10-29")
#     page.get_by_role("button", name="View Report").click()
#     page.get_by_text("×Close").click()
#     page.locator("nav").filter(has_text="nazianazia01Change").locator("svg").click()
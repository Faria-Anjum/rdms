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
        expect(self.page.get_by_role("link", name=self.title, exact=True)).to_be_visible()
        self.page.get_by_role("link", name=self.title, exact=True).click()
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
    
class DeviceLifetimeTracking(SimActivationReport):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/device-life-time-tracking"
        self.title = "Device Life Time Tracking"

    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_text("Device Lifetime Tracking Report")).to_be_visible()

class DeviceStatus(SimActivationReport): #twoyears
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/device-status"
        self.title = "Device Status"

    def clickReport(self):
        return Dashboard.clickReport(self)
    
class CentralInventoryStock(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/central-inventory-stock"
        self.title = "Central Inventory Stock"

class DeviceRegistrationReport(ActivationDetails): #onemonth
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/device-registration"
        self.title = "Device Registration Report"
        # self.datefromloc = "input[name=\"regFromDate\"]"
        # self.datetoloc = "input[name=\"regToDate\"]"
    

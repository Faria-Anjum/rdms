from playwright.sync_api import expect
from models.main import Dashboard
from models.reports import ActivationDetails, SimActivationReport

class UserManagement(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/user-management-information"
        self.title = "User Management"

    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_text("User Management and Information Report")).to_be_visible()

class DistributorInformation(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/distributor-information"
        self.title = "Distributor Information"

class ProductMasterData(ActivationDetails):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/product-master-data"
        self.title = "Product Master Data"

class DsrMasterData(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/dsr-master-data"
        self.title = "Dsr Master Data"

class DsrRouteInformation(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/dsr-route-information"
        self.title = "Dsr Route Information"

class DsrRouteInformation(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/dsr-route-information"
        self.title = "Dsr Route Information"

class RetailerMasterData(SimActivationReport):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/retailer-master-data"
        self.title = "Retailer Master Data"
    
    def clickReport(self):
        return Dashboard.clickReport(self)

class RetailerRegRequest(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/retailer/retailer-registration-request"
        self.title = "Retailer Reg. Request"

    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_text("Retailer Registration Request Report")).to_be_visible()

class RetailerModificationRequest(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/retailer-modification-request"
        self.title = "Retailer Modification Request"

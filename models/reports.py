from playwright.sync_api import expect
from models.main import Dashboard

class SoPayment(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/so-payment"
        self.title = "SO Payment"

    def clickSoReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_text("Sales Order"+self.title[2:])).to_be_visible()

class SoMisReport(SoPayment):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/so-mis-report"
        self.title = "SO MIS Report"

class SimStock(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/sim-stock"
        self.title = "Sim Stock"

class ScStock(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/sc-stock"
        self.title = "SC Stock"

class ActivationDetails(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/activation-report"
        self.title = "Activation Report (Details)"
        self.datefromloc = "input[name=\"activationDateFrom\"]"
        self.datetoloc = "input[name=\"activationDateTo\"]"

    #method overriding
    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_role("main").get_by_text(self.title)).to_be_visible()
        expect(self.page).to_have_url(self.url)

class ActivationSummary(ActivationDetails):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/activation-report-summary"
        self.title = "Activation Report (Summary)"
        self.datefromloc = "input[name=\"activationDateFrom\"]"
        self.datetoloc = "input[name=\"activationDateTo\"]"

class DeliveryDetails(ActivationDetails):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/delivery-report"
        self.title = "Delivery Report (Details)"
        self.datefromloc = "input[name=\"deliveryFromDate\"]"
        self.datetoloc = "input[name=\"deliveryToDate\"]"

class DeliverySummary(ActivationDetails):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/delivery-report-summary"
        self.title = "Delivery Report (Summary)"
        self.datefromloc = "input[name=\"deliveryFromDate\"]"
        self.datetoloc = "input[name=\"deliveryToDate\"]"

class DeliveryVsActivation(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/delivery-vs-activation-summary"
        self.title = "Delivery vs Activation ("
        self.datefromloc = "input[name=\"activationDateFrom\"]"
        self.datetoloc = "input[name=\"activationDateTo\"]"
        self.seconddatefrom = "input[name=\"deliveryFromDate\"]"
        self.seconddateto = "input[name=\"deliveryToDate\"]"

    #method overriding, overloading
    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_role("main").get_by_text("Delivery vs Activation Summary")).to_be_visible()
        expect(self.page).to_have_url(self.url)

class RealTimeActivation(ActivationDetails):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/real-time-activation"
        self.title = "Real Time Activation (Details)"

class RetailerStock(ActivationDetails):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/retailer-stock-details"
        self.title = "Retailer Stock (Details)"
        self.datefromloc = "input[name=\"liftingFromDate\"]"
        self.datetoloc = "input[name=\"liftingToDate\"]"

class NoActivatedMsisdn(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/no-activated-msisdn-details"
        self.title = "No Activated MSISDN (Details)"
        self.datefromloc = "input[name=\"liftingFromDate\"]"
        self.datetoloc = "input[name=\"liftingToDate\"]"

class LiftingVsActivation(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/lifting-vs-activation-summary"
        self.title = "Lifting vs Activation ("
        self.datefromloc = "input[name=\"liftingFromDate\"]"
        self.datetoloc = "input[name=\"liftingToDate\"]"
        self.seconddatefrom = "input[name=\"activationDateFrom\"]"
        self.seconddateto = "input[name=\"activationDateTo\"]"

    #method overriding, overloading
    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_role("main").get_by_text("Lifting vs Activation (Summary)")).to_be_visible()
        expect(self.page).to_have_url(self.url)

class PendingSimODReport(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/pending/od/sim"
        self.title = "Pending OD Report(SIM)"
        self.datefromloc = "input[name=\"registrationFromDate\"]"
        self.datetoloc = "input[name=\"registrationToDate\"]"

    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_role("main").get_by_text("Pending SIM OD Report")).to_be_visible()
        expect(self.page).to_have_url(self.url)

class PendingSCODReport(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/pending/od/sc"
        self.title = "Pending OD Report(SC)"
        self.datefromloc = "input[name=\"registrationFromDate\"]"
        self.datetoloc = "input[name=\"registrationToDate\"]"

    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_role("main").get_by_text("Pending SC OD Report")).to_be_visible()
        expect(self.page).to_have_url(self.url)

class SimActivationReport(ActivationDetails):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/sim-activation"
        self.title = "Sim Activation Report"

    def enterDateFromTo(self, today, month):
        expect(self.page.locator("input[name=\"fromDate\"]")).to_be_visible()
        self.page.locator("input[name=\"fromDate\"]").fill(month)
        expect(self.page.locator("input[name=\"toDate\"]")).to_be_visible()
        self.page.locator("input[name=\"toDate\"]").fill(today)

class SalesCallDSR(SimActivationReport):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/sales-call-by-dsr"
        self.title = "Sales Call (By DSR)"

    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_role("main").get_by_text("Sales Call Report "+self.title[11:])).to_be_visible()
        expect(self.page).to_have_url(self.url)

class SalesCallTransac(SalesCallDSR):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/sales-call-by-transaction"
        self.title = "Sales Call (By Transaction)"

    def enterDateFromTo(self, today, month):
        self.page.get_by_role("textbox").first.fill(month)
        self.page.get_by_role("textbox").nth(1).fill(today)

class MarketVisitPlan(SimActivationReport):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/market-visit-plan"
        self.title = "Market Visit Plan"

    def clickReport(self):
        return Dashboard.clickReport(self)
    
class MarketVisitRoutewise(SimActivationReport):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/routewise-market-visit"
        self.title = "Market Visit (Routewise)"

    def clickReport(self):
        expect(self.page.get_by_role("link", name=self.title)).to_be_visible()
        self.page.get_by_role("link", name=self.title).click()
        expect(self.page.get_by_role("main").get_by_text("Routewise Market Visit Report")).to_be_visible()
        expect(self.page).to_have_url(self.url)

class BPPerformance(Dashboard):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/bp-performance"
        self.title = "BP Performance"
        self.datefromloc = "input[name=\"activationDateFrom\"]"
        self.datetoloc = "input[name=\"activationDateTo\"]"
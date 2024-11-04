from models.main import LoginPage
from models.reports import SalesCallRetailer

def test_findSalesCallReport(page):

    '''User can navigate to Sales Call Report (Retailer)'''
    retailer = SalesCallRetailer(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    retailer.findReport()
    
def test_navSalesCallReport(page):
    '''User can navigate to Sales Call Report (Retailer)'''
    retailer = SalesCallRetailer(page)
    retailer.clickReport()

def test_enterDate(page, today, onemonth):
    '''User can enter date range for Sales Call Report (Retailer)'''
    retailer = SalesCallRetailer(page)
    retailer.enterDateFromTo(today, onemonth)
    
def test_viewSalesCallReport(page):
    '''User can click to view Sales Call Report (Retailer)'''
    retailer = SalesCallRetailer(page)
    retailer.viewReport()

def test_closeSalesCallReport(page):
    '''Sales Call Report (Retailer) loads sucessfully'''
    retailer = SalesCallRetailer(page)
    retailer.closeReport()
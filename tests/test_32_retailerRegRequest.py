from models.main import LoginPage
from models.masterDataReports import RetailerRegRequest
    
def test_navRetailerRegRequest(page):
    '''User can navigate to Retailer Registration Request Report and select filters'''
    retailerreg = RetailerRegRequest(page)
    retailerreg.clickReport()

def test_enterDate(page, today, onemonth):
    '''User can enter date range for Retailer Registration Request Report'''
    retailerreg = RetailerRegRequest(page)
    retailerreg.enterDateFromTo(today, onemonth)
    
def test_viewRetailerRegRequest(page):
    '''User can click to view Retailer Registration Request Report'''
    retailerreg = RetailerRegRequest(page)
    retailerreg.viewReport()

def test_closeRetailerRegRequest(page):
    '''Retailer Registration Request Report loads sucessfully'''
    retailerreg = RetailerRegRequest(page)
    retailerreg.closeReport()
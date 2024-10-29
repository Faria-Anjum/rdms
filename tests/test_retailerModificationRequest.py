from models.main import LoginPage
from models.masterDataReports import RetailerModificationRequest

def test_findRetailerModificationRequest(page):
    '''User can navigate to Retailer Modification Request Report'''
    retailermod = RetailerModificationRequest(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    retailermod.findMasterDataReport()
    
def test_navRetailerModificationRequest(page):
    '''User can navigate to Retailer Modification Request Report and select filters'''
    retailermod = RetailerModificationRequest(page)
    retailermod.clickReport()

def test_enterDate(page, today, onemonth):
    '''User can enter date range for Retailer Modification Request Report'''
    retailermod = RetailerModificationRequest(page)
    retailermod.enterDateFromTo(today, onemonth)
    
def test_viewRetailerModificationRequest(page):
    '''User can click to view Retailer Modification Request Report'''
    retailermod = RetailerModificationRequest(page)
    retailermod.viewReport()

def test_closeRetailerModificationRequest(page):
    '''Retailer Modification Request Report loads sucessfully'''
    retailermod = RetailerModificationRequest(page)
    retailermod.closeReport()
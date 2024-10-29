from models.main import LoginPage
from models.masterDataReports import RetailerMasterData

def test_findRetailerMasterData(page):
    '''User can navigate to Retailer Master Data Report'''
    retailermaster = RetailerMasterData(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    retailermaster.findMasterDataReport()
    
def test_navRetailerMasterData(page):
    '''User can navigate to Retailer Master Data Report and select filters'''
    retailermaster = RetailerMasterData(page)
    retailermaster.clickReport()

def test_enterDate(page):
    '''User can enter date range for Retailer Master Data Report'''
    retailermaster = RetailerMasterData(page)
    retailermaster.enterDateFromTo()
    
def test_viewRetailerMasterData(page):
    '''User can click to view Retailer Master Data Report'''
    retailermaster = RetailerMasterData(page)
    retailermaster.viewReport()

def test_closeRetailerMasterData(page):
    '''Retailer Master Data Report loads sucessfully'''
    retailermaster = RetailerMasterData(page)
    retailermaster.closeReport()
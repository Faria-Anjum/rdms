from models.main import LoginPage
from models.reports import RetailerStock
    
def test_navRetailerStock(page):
    '''User can navigate to Retailer Stock Details and select filters'''
    retail = RetailerStock(page)
    retail.clickReport()

def test_enterDate(page, today, twomonths):
    '''User can enter date range for Retailer Stock Details'''
    retail = RetailerStock(page)
    retail.enterDateFromTo(today, twomonths)
    
def test_viewRetailerStock(page):
    '''User can click to view Retailer Stock Details'''
    retail = RetailerStock(page)
    retail.viewReport()

def test_closeRetailerStock(page):
    '''Retailer Stock Details loads sucessfully'''
    retail = RetailerStock(page)
    retail.closeReport()
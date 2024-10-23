from models.main import LoginPage, RetailerStock

def test_findRetailerStock(page):
    '''User can navigate to Retailer Stock Details'''
    retail = RetailerStock(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    retail.findReport()
    
def test_navRetailerStock(page):
    '''User can navigate to Retailer Stock Details and select filters'''
    retail = RetailerStock(page)
    retail.clickReport()

def test_enterDate(page):
    '''User can enter date range for Retailer Stock Details'''
    retail = RetailerStock(page)
    retail.enterDateFromTo()
    
def test_viewRetailerStock(page):
    '''User can click to view Retailer Stock Details'''
    retail = RetailerStock(page)
    retail.viewReport()

def test_closeRetailerStock(page):
    '''Retailer Stock Details loads sucessfully'''
    retail = RetailerStock(page)
    retail.closeReport()
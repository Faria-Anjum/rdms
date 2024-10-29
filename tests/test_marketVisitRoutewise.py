from models.main import LoginPage
from models.reports import MarketVisitRoutewise

def test_findMarketVisitRoutewise(page):
    '''User can navigate to Routewise Market Visit Report'''
    marketroute = MarketVisitRoutewise(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    marketroute.findReport()
    
def test_navMarketVisitRoutewise(page):
    '''User can navigate to Routewise Market Visit Report and select filters'''
    marketroute = MarketVisitRoutewise(page)
    marketroute.clickReport()

def test_enterDate(page):
    '''User can enter date range for Routewise Market Visit Report'''
    marketroute = MarketVisitRoutewise(page)
    marketroute.enterDateFromTo()
    
def test_viewMarketVisitRoutewise(page):
    '''User can click to view Routewise Market Visit Report'''
    marketroute = MarketVisitRoutewise(page)
    marketroute.viewReport()

def test_closeMarketVisitRoutewise(page):
    '''Routewise Market Visit Report loads sucessfully'''
    marketroute = MarketVisitRoutewise(page)
    marketroute.closeReport()
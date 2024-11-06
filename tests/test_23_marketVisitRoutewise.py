from models.main import LoginPage
from models.reports import MarketVisitRoutewise
    
def test_navMarketVisitRoutewise(page):
    '''User can navigate to Routewise Market Visit Report and select filters'''
    marketroute = MarketVisitRoutewise(page)
    marketroute.clickReport()

def test_enterDate(page, today, onemonth):
    '''User can enter date range for Routewise Market Visit Report'''
    marketroute = MarketVisitRoutewise(page)
    marketroute.enterDateFromTo(today, onemonth)
    
def test_viewMarketVisitRoutewise(page):
    '''User can click to view Routewise Market Visit Report'''
    marketroute = MarketVisitRoutewise(page)
    marketroute.viewReport()

def test_closeMarketVisitRoutewise(page):
    '''Routewise Market Visit Report loads sucessfully'''
    marketroute = MarketVisitRoutewise(page)
    marketroute.closeReport()
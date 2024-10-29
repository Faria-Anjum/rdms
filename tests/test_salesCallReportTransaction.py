from models.main import LoginPage
from models.reports import SalesCallTransac

def test_findSalesCallReport(page):
    '''User can navigate to Sales Call Report (Transaction)'''
    transac = SalesCallTransac(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    transac.findReport()
    
def test_navSalesCallReport(page):
    '''User can navigate to Sales Call Report (Transaction) and select filters'''
    transac = SalesCallTransac(page)
    transac.clickReport()

def test_enterDate(page):
    '''User can enter date range for Sales Call Report (Transaction)'''
    transac = SalesCallTransac(page)
    transac.enterDateFromTo()
    
def test_viewSalesCallReport(page):
    '''User can click to view Sales Call Report (Transaction)'''
    transac = SalesCallTransac(page)
    transac.viewReport()

def test_closeSalesCallReport(page):
    '''Sales Call Report (Transaction) loads sucessfully'''
    transac = SalesCallTransac(page)
    transac.closeReport()
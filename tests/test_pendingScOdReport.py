from models.main import LoginPage
from models.reports import PendingSCODReport

def test_findPendingSCODReport(page):

    '''User can navigate to Pending SC OD Report'''
    od = PendingSCODReport(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    od.findReport()
    
def test_navPendingSCODReport(page):
    '''User can navigate to Pending SC OD report and select filters'''
    od = PendingSCODReport(page)
    od.clickReport()

def test_enterDate(page, today, onemonth):
    '''User can enter date range for Pending SC OD Report'''
    od = PendingSCODReport(page)
    od.enterDateFromTo(today, onemonth)
    
def test_viewPendingSCODReport(page):
    '''User can click to view Pending SC OD Report'''
    od = PendingSCODReport(page)
    od.viewReport()

def test_closePendingSCODReport(page):
    '''Pending SC OD Report loads sucessfully'''
    od = PendingSCODReport(page)
    od.closeReport()
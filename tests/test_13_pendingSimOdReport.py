from models.main import LoginPage
from models.reports import PendingSimODReport
    
def test_navPendingSimODReport(page):
    '''User can navigate to Pending Sim OD Report and select filters'''
    od = PendingSimODReport(page)
    od.clickReport()

def test_enterDate(page, today, onemonth):
    '''User can enter date range for Pending Sim OD Report'''
    od = PendingSimODReport(page)
    od.enterDateFromTo(today, onemonth)
    
def test_viewPendingSimODReport(page):
    '''User can click to view Pending Sim OD Report'''
    od = PendingSimODReport(page)
    od.viewReport()

def test_closePendingSimODReport(page):
    '''Pending Sim OD Report loads sucessfully'''
    od = PendingSimODReport(page)
    od.closeReport()
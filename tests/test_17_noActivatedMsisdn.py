from models.main import LoginPage
from models.reports import NoActivatedMsisdn
    
def test_navNoActivatedMsisdn(page):
    '''User can navigate to No Activated MSISDN Details Report and select filters'''
    activeMsisdn = NoActivatedMsisdn(page)
    activeMsisdn.clickReport()

def test_enterDate(page, today, twomonths):
    '''User can enter date range for No Activated MSISDN Details Report'''
    activeMsisdn = NoActivatedMsisdn(page)
    activeMsisdn.enterDateFromTo(today, twomonths)
    
def test_viewNoActivatedMsisdn(page):
    '''User can click to view No Activated MSISDN Details Report'''
    activeMsisdn = NoActivatedMsisdn(page)
    activeMsisdn.viewReport()

def test_closeNoActivatedMsisdn(page):
    '''No Activated MSISDN Details Report loads sucessfully'''
    activeMsisdn = NoActivatedMsisdn(page)
    activeMsisdn.closeReport()
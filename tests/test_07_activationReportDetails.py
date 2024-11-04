from models.main import LoginPage
from models.reports import ActivationDetails
    
def test_navActivationReport(page):
    '''User can navigate to Activation Details Report and select filters'''
    activ = ActivationDetails(page)
    activ.clickReport()

def test_enterDate(page, today, onemonth):
    '''User can enter date range for Activation Details Report'''
    activ = ActivationDetails(page)
    activ.enterDateFromTo(today, onemonth)
    
def test_viewActivationReport(page):
    '''User can click to view Activation Details Report'''
    activ = ActivationDetails(page)
    activ.viewReport()

def test_closeActivationReport(page):
    '''Activation Details Report loads sucessfully'''
    activ = ActivationDetails(page)
    activ.closeReport()
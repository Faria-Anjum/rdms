from models.main import LoginPage
from models.reports import ActivationSummary
    
def test_navActivationReport(page):
    '''User can navigate to Activation Summary Report and select filters'''
    activ = ActivationSummary(page)
    activ.clickReport()

def test_enterDate(page, today, onemonth):
    '''User can enter date range for Activation Summary Report'''
    activ = ActivationSummary(page)
    activ.enterDateFromTo(today, onemonth)
    
def test_viewActivationReport(page):
    '''User can click to view Activation Summary Report'''
    activ = ActivationSummary(page)
    #pytest.xfail(activ.viewReport())
    activ.viewReport()

def test_closeActivationReport(page):
    '''Activation Summary Report loads sucessfully'''
    activ = ActivationSummary(page)
    activ.closeReport()
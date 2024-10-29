from models.main import LoginPage
from models.reports import SimActivationReport

def test_findSimActivationReport(page):

    '''User can navigate to Sim Activation Report'''
    simactiv = SimActivationReport(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    simactiv.findReport()
    
def test_navSimActivationReport(page):
    '''User can navigate to Sim Activation Report and select filters'''
    simactiv = SimActivationReport(page)
    simactiv.clickReport()

def test_enterDate(page):
    '''User can enter date range for Sim Activation Report'''
    simactiv = SimActivationReport(page)
    simactiv.enterDateFromTo()
    
def test_viewSimActivationReport(page):
    '''User can click to view Sim Activation Report'''
    simactiv = SimActivationReport(page)
    simactiv.viewReport()

def test_closeSimActivationReport(page):
    '''Sim Activation Report loads sucessfully'''
    simactiv = SimActivationReport(page)
    simactiv.closeReport()
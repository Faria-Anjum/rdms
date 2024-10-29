from models.main import LoginPage
from models.reports import LiftingVsActivation

def test_findLiftingVsActivationReport(page):
    '''User can navigate to Lifting vs Activation Summary Report'''
    liftvsactiv = LiftingVsActivation(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    liftvsactiv.findReport()
    
def test_navLiftingVsActivationReport(page):
    '''User can navigate to Lifting vs Activation Summary Report and select filters'''
    liftvsactiv = LiftingVsActivation(page)
    liftvsactiv.clickReport()

def test_enterDate(page, today, twomonths):
    '''User can enter date range for Lifting vs Activation Summary Report'''
    liftvsactiv = LiftingVsActivation(page)
    liftvsactiv.enterDateFromTo(today, twomonths)
    liftvsactiv.enterSecondDateFromTo(today, twomonths)
    
def test_viewLiftingVsActivationReport(page):
    '''User can click to view Lifting vs Activation Summary Report'''
    liftvsactiv = LiftingVsActivation(page)
    liftvsactiv.viewReport()

def test_closeLiftingVsActivationReport(page):
    '''Lifting vs Activation Summary Report loads sucessfully'''
    liftvsactiv = LiftingVsActivation(page)
    liftvsactiv.closeReport()
from models.main import LoginPage, LiftingVsActivation

def test_findDeliveryVsActivationReport(page):
    '''User can navigate to Lifting vs Activation Summary Report'''
    liftvsactiv = LiftingVsActivation(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    liftvsactiv.findReport()
    
def test_navDeliveryVsActivationReport(page):
    '''User can navigate to Lifting vs Activation Summary Report and select filters'''
    liftvsactiv = LiftingVsActivation(page)
    liftvsactiv.clickReport()

def test_enterDate(page):
    '''User can enter date range for Lifting vs Activation Summary Report'''
    liftvsactiv = LiftingVsActivation(page)
    liftvsactiv.enterDateFromTo()
    liftvsactiv.enterSecondDateFromTo()
    
def test_viewDeliveryVsActivationReport(page):
    '''User can click to view Lifting vs Activation Summary Report'''
    liftvsactiv = LiftingVsActivation(page)
    liftvsactiv.viewReport()

def test_closeDeliveryVsActivationReport(page):
    '''Lifting vs Activation Summary Report loads sucessfully'''
    liftvsactiv = LiftingVsActivation(page)
    liftvsactiv.closeReport()
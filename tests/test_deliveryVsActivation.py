from models.main import LoginPage, DeliveryVsActivation

def test_findDeliveryVsActivationReport(page):
    '''User can navigate to Delivery vs Activation Summary Report'''
    delvsactiv = DeliveryVsActivation(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    delvsactiv.findReport()
    
def test_navDeliveryVsActivationReport(page):
    '''User can navigate to Delivery vs Activation Summary Report and select filters'''
    delvsactiv = DeliveryVsActivation(page)
    delvsactiv.clickReport()

def test_enterDate(page):
    '''User can enter date range for Delivery vs Activation Summary Report'''
    delvsactiv = DeliveryVsActivation(page)
    delvsactiv.enterDateFromTo()
    delvsactiv.enterSecondDateFromTo()
    
def test_viewDeliveryVsActivationReport(page):
    '''User can click to view Delivery vs Activation Summary Report'''
    delvsactiv = DeliveryVsActivation(page)
    delvsactiv.viewReport()

def test_closeDeliveryVsActivationReport(page):
    '''Delivery vs Activation Summary Report loads sucessfully'''
    delvsactiv = DeliveryVsActivation(page)
    delvsactiv.closeReport()
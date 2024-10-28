from models.main import LoginPage, SalesCallDSR

def test_findSalesCallReport(page):

    '''User can navigate to Sales Call Report (DSR)'''
    dsr = SalesCallDSR(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    dsr.findReport()
    
def test_navSalesCallReport(page):
    '''User can navigate to Sales Call Report (DSR) and select filters'''
    dsr = SalesCallDSR(page)
    dsr.clickReport()

def test_enterDate(page):
    '''User can enter date range for Sales Call Report (DSR)'''
    dsr = SalesCallDSR(page)
    dsr.enterDateFromTo()
    
def test_viewSalesCallReport(page):
    '''User can click to view Sales Call Report (DSR)'''
    dsr = SalesCallDSR(page)
    dsr.viewReport()

def test_closeSalesCallReport(page):
    '''Sales Call Report (DSR) loads sucessfully'''
    dsr = SalesCallDSR(page)
    dsr.closeReport()
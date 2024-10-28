from models.main import LoginPage, PendingSimODReport

def test_findPendingSimODReport(page):

    '''User can navigate to Pending Sim OD Report'''
    od = PendingSimODReport(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    od.findReport()
    
def test_navPendingSimODReport(page):
    '''User can navigate to Pending Sim OD report and select filters'''
    od = PendingSimODReport(page)
    od.clickReport()

def test_enterDate(page):
    '''User can enter date range for Pending Sim OD Report'''
    od = PendingSimODReport(page)
    od.enterDateFromTo()
    
def test_viewPendingSimODReport(page):
    '''User can click to view Pending Sim OD Report'''
    od = PendingSimODReport(page)
    od.viewReport()

def test_closePendingSimODReport(page):
    '''Pending Sim OD Report loads sucessfully'''
    od = PendingSimODReport(page)
    od.closeReport()
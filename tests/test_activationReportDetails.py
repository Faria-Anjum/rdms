from models.main import LoginPage, ActivationDetails

def test_findActivationReport(page):
    # context = browser.new_context(storage_state='auth.json')
    # page = context.new_page()

    '''User can navigate to Activation Details Report'''
    activ = ActivationDetails(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    activ.findReport()
    
def test_navActivationReport(page):
    '''User can navigate to Activation Details report and select filters'''
    activ = ActivationDetails(page)
    activ.clickReport()

def test_enterDate(page):
    '''User can enter date range for Activation Details Report'''
    activ = ActivationDetails(page)
    activ.enterDate()
    
def test_viewActivationReport(page):
    '''User can click to view Activation Details Report'''
    activ = ActivationDetails(page)
    #pytest.xfail(activ.viewReport())
    activ.viewReport()

def test_closeActivationReport(page):
    '''Activation Details Report loads sucessfully'''
    activ = ActivationDetails(page)
    activ.closeReport()
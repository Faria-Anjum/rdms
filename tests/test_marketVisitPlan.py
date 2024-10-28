from models.main import LoginPage, MarketVisitPlan

def test_findMarketVisitPlan(page):
    '''User can navigate to Market Visit Plan Report'''
    marketplan = MarketVisitPlan(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    marketplan.findReport()
    
def test_navMarketVisitPlan(page):
    '''User can navigate to Market Visit Plan Report and select filters'''
    marketplan = MarketVisitPlan(page)
    marketplan.clickReport()

def test_enterDate(page):
    '''User can enter date range for Market Visit Plan Report'''
    marketplan = MarketVisitPlan(page)
    marketplan.enterDateFromTo()
    
def test_viewMarketVisitPlan(page):
    '''User can click to view Market Visit Plan Report'''
    marketplan = MarketVisitPlan(page)
    marketplan.viewReport()

def test_closeMarketVisitPlan(page):
    '''Market Visit Plan Report loads sucessfully'''
    marketplan = MarketVisitPlan(page)
    marketplan.closeReport()
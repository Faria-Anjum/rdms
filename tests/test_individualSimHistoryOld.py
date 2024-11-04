from models.main import LoginPage
from models.reports import IndividualSimHistoryOld

def test_findIndividualSimHistoryOld(page):
    '''User can navigate to Individual Sim History (Old) Report'''
    indivhistoryold = IndividualSimHistoryOld(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    indivhistoryold.findReport()
    
def test_navIndividualSimHistoryOld(page):
    '''User can navigate to Individual Sim History (Old) Report'''
    indivhistoryold = IndividualSimHistoryOld(page)
    indivhistoryold.clickReport()

def test_enterText(page):
    '''User can enter MSISDN for Individual Sim History (Old) Report'''
    indivhistoryold = IndividualSimHistoryOld(page)
    indivhistoryold.enterText()
    indivhistoryold.selectMSISDN()
    
def test_viewIndividualSimHistoryOld(page):
    '''User can click to view Individual Sim History (Old) Report'''
    indivhistoryold = IndividualSimHistoryOld(page)
    indivhistoryold.viewReport()

def test_noIndividualSimHistoryOld(page):
    '''User receives No Data Found error'''
    indivhistoryold = IndividualSimHistoryOld(page)
    indivhistoryold.noDataFound()
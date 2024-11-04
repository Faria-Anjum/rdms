from models.main import LoginPage
from models.reports import IndividualSimHistory

def test_findIndividualSimHistory(page):
    '''User can navigate to Individual Sim History Report'''
    indivhistory = IndividualSimHistory(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    indivhistory.findReport()
    
def test_navIndividualSimHistory(page):
    '''User can navigate to Individual Sim History Report'''
    indivhistory = IndividualSimHistory(page)
    indivhistory.clickReport()

def test_enterText(page):
    '''User can enter MSISDN for Individual Sim History Report'''
    indivhistory = IndividualSimHistory(page)
    indivhistory.enterText()
    indivhistory.selectMSISDN()
    
def test_viewIndividualSimHistory(page):
    '''User can click to view Individual Sim History Report'''
    indivhistory = IndividualSimHistory(page)
    indivhistory.viewReport()

def test_noIndividualSimHistory(page):
    '''User receives No Data Found error'''
    indivhistory = IndividualSimHistory(page)
    indivhistory.noDataFound()
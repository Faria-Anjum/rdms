from models.main import LoginPage
from models.deviceReports import IndividualDeviceTransactionHistory

def test_findIndividualDeviceTransaction(page):
    '''User can navigate to Individual Device Transaction History Report'''
    indivdevicetransac = IndividualDeviceTransactionHistory(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    indivdevicetransac.findDeviceReports()
    
def test_navIndividualDeviceTransaction(page):
    '''User can navigate to Individual Device Transaction History Report and select filters'''
    indivdevicetransac = IndividualDeviceTransactionHistory(page)
    indivdevicetransac.clickReport()

def test_enterIMEI(page, today, onemonth):
    '''User can enter device IMEI for Individual Device Transaction History Report'''
    indivdevicetransac = IndividualDeviceTransactionHistory(page)
    indivdevicetransac.fillTextbox()
    
def test_viewIndividualDeviceTransaction(page):
    '''User can click to view Individual Device Transaction History Report'''
    indivdevicetransac = IndividualDeviceTransactionHistory(page)
    indivdevicetransac.viewReport()

def test_closeIndividualDeviceTransaction(page):
    '''Individual Device Transaction History Report loads sucessfully'''
    indivdevicetransac = IndividualDeviceTransactionHistory(page)
    indivdevicetransac.closeReport()
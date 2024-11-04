from models.main import LoginPage
from models.deviceReports import IndividualDeviceHistory

def test_findIndividualDeviceHistory(page):
    '''User can navigate to Individual Device History Report'''
    indivdevicehistory = IndividualDeviceHistory(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    indivdevicehistory.findDeviceReports()
    
def test_navIndividualDeviceHistory(page):
    '''User can navigate to Individual Device History Report and select filters'''
    indivdevicehistory = IndividualDeviceHistory(page)
    indivdevicehistory.clickReport()

def test_enterIMEI(page, today, onemonth):
    '''User can enter device IMEI for Individual Device History Report'''
    indivdevicehistory = IndividualDeviceHistory(page)
    indivdevicehistory.fillTextbox()
    
def test_viewIndividualDeviceHistory(page):
    '''User can click to view Individual Device History Report'''
    indivdevicehistory = IndividualDeviceHistory(page)
    indivdevicehistory.viewReport()

def test_noIndividualDeviceHistory(page):
    '''User receives No Data Found error'''
    indivdevicehistory = IndividualDeviceHistory(page)
    indivdevicehistory.noDataFound()
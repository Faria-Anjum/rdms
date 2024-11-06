from models.main import LoginPage
from models.deviceReports import DeviceRegistrationReport
    
def test_navDeviceRegistrationReport(page):
    '''User can navigate to Device Registration Report and select filters'''
    devicereg = DeviceRegistrationReport(page)
    devicereg.clickReport()

def test_viewDeviceRegistrationReport(page):
    '''User can click to view Device Registration Report'''
    devicereg = DeviceRegistrationReport(page)
    devicereg.viewReport()

def test_closeDeviceRegistrationReport(page):
    '''Device Registration Report loads sucessfully'''
    devicereg = DeviceRegistrationReport(page)
    devicereg.closeReport()
from models.main import LoginPage
from models.deviceReports import DeviceTransaction
    
def test_navDeviceTransaction(page):
    '''User can navigate to Device Transaction Report and select filters'''
    devicetransac = DeviceTransaction(page)
    devicetransac.clickReport()
    
def test_enterDate(page, twomonths):
    '''User can enter date range for Device Transaction Report'''
    sim = DeviceTransaction(page)
    sim.enterDateFrom(twomonths)

def test_viewDeviceTransaction(page):
    '''User can click to view Device Transaction Report'''
    devicetransac = DeviceTransaction(page)
    devicetransac.viewReport()

def test_noDeviceTransaction(page):
    '''User receives No Data Found error'''
    devicetransac = DeviceTransaction(page)
    devicetransac.noDataFound()
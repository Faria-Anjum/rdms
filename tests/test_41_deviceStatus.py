from models.main import LoginPage
from models.deviceReports import DeviceStatus
    
def test_navDeviceStatus(page):
    '''User can navigate to Device Status Report and select filters'''
    devicestatus = DeviceStatus(page)
    devicestatus.clickReport()
    
def test_enterDate(page, twoyears):
    '''User can enter date range for Device Status Report'''
    sim = DeviceStatus(page)
    sim.enterDateFrom(twoyears)

def test_viewDeviceStatus(page):
    '''User can click to view Device Status Report'''
    devicestatus = DeviceStatus(page)
    devicestatus.viewReport()

def test_closeDeviceStatus(page):
    '''Device Status Report loads sucessfully'''
    devicestatus = DeviceStatus(page)
    devicestatus.closeReport()
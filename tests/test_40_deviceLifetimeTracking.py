from models.main import LoginPage
from models.deviceReports import DeviceLifetimeTracking
    
def test_navDeviceLifetimeTracking(page):
    '''User can navigate to Device Lifetime Tracking Report and select filters'''
    devicelifetime = DeviceLifetimeTracking(page)
    devicelifetime.clickReport()
    
def test_enterDate(page, twoyears):
    '''User can enter date range for Device Lifetime Tracking Report'''
    sim = DeviceLifetimeTracking(page)
    sim.enterDateFrom(twoyears)

def test_viewDeviceLifetimeTracking(page):
    '''User can click to view Device Lifetime Tracking Report'''
    devicelifetime = DeviceLifetimeTracking(page)
    devicelifetime.viewReport()

def test_closeDeviceLifetimeTracking(page):
    '''Device Lifetime Tracking Report loads sucessfully'''
    devicelifetime = DeviceLifetimeTracking(page)
    devicelifetime.closeReport()
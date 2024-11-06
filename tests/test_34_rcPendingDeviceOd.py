from models.main import LoginPage
from models.deviceReports import RCPendingDeviceOD
    
def test_navRCPendingDeviceOD(page):
    '''User can navigate to RC Pending Device OD Report and select filters'''
    rcpendingod = RCPendingDeviceOD(page)
    rcpendingod.findDeviceReports()
    rcpendingod.clickReport()
    
def test_enterDate(page, twoyears):
    '''User can enter date range for RC Pending Device OD Report'''
    sim = RCPendingDeviceOD(page)
    sim.enterDateFrom(twoyears)

def test_viewRCPendingDeviceOD(page):
    '''User can click to view RC Pending Device OD Report'''
    rcpendingod = RCPendingDeviceOD(page)
    rcpendingod.viewReport()

def test_closeRCPendingDeviceOD(page):
    '''RC Pending Device OD Report loads sucessfully'''
    rcpendingod = RCPendingDeviceOD(page)
    rcpendingod.closeReport()
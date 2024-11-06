from models.main import LoginPage
from models.deviceReports import PendingDeviceOD
    
def test_navPendingDeviceOD(page):
    '''User can navigate to Pending Device OD Report and select filters'''
    pendingod = PendingDeviceOD(page)
    pendingod.clickReport()
    
def test_enterDate(page, twoyears):
    '''User can enter date range for Pending Device OD Report'''
    sim = PendingDeviceOD(page)
    sim.enterDateFrom(twoyears)

def test_viewPendingDeviceOD(page):
    '''User can click to view Pending Device OD Report'''
    pendingod = PendingDeviceOD(page)
    pendingod.viewReport()

def test_closePendingDeviceOD(page):
    '''Pending Device OD Report loads sucessfully'''
    pendingod = PendingDeviceOD(page)
    pendingod.closeReport()
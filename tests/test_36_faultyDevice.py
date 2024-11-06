from models.main import LoginPage
from models.deviceReports import FaultyDevice
    
def test_navFaultyDevice(page):
    '''User can navigate to Faulty Device Report and select filters'''
    faulty = FaultyDevice(page)
    faulty.clickReport()
    
def test_enterDate(page, twoyears):
    '''User can enter date range for Faulty Device Report'''
    sim = FaultyDevice(page)
    sim.enterDateFrom(twoyears)

def test_viewFaultyDevice(page):
    '''User can click to view Faulty Device Report'''
    faulty = FaultyDevice(page)
    faulty.viewReport()

def test_noFaultyDevice(page):
    '''User receives No Data Found error'''
    faulty = FaultyDevice(page)
    faulty.noDataFound()
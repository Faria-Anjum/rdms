from models.main import LoginPage
from models.reports import RealTimeActivation
    
def test_navRealTimeActivationReport(page):
    '''User can navigate to Real Time Activation Report Details and select filters'''
    realtime = RealTimeActivation(page)
    realtime.clickReport()
    
def test_viewRealTimeActivationReport(page):
    '''User can click to view Real Time Activation Report Details'''
    realtime = RealTimeActivation(page)
    realtime.viewReport()

def test_closeRealTimeActivationReport(page):
    '''Real Time Activation Report Details loads sucessfully'''
    realtime = RealTimeActivation(page)
    realtime.closeReport()
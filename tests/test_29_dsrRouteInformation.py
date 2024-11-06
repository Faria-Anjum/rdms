from models.main import LoginPage
from models.masterDataReports import DsrRouteInformation
    
def test_navDsrRouteInformation(page):
    '''User can navigate to Dsr Route Information Report and select filters'''
    dsrroute = DsrRouteInformation(page)
    dsrroute.clickReport()
    
def test_viewDsrRouteInformation(page):
    '''User can click to view Dsr Route Information Report'''
    dsrroute = DsrRouteInformation(page)
    dsrroute.viewReport()

def test_closeDsrRouteInformation(page):
    '''Dsr Route Information Report loads sucessfully'''
    dsrroute = DsrRouteInformation(page)
    dsrroute.closeReport()
from models.main import LoginPage
from models.masterDataReports import DsrMasterData
    
def test_navDsrMasterData(page):
    '''User can navigate to Dsr Master Data Report and select filters'''
    dsrmaster = DsrMasterData(page)
    dsrmaster.clickReport()
    
def test_viewDsrMasterData(page):
    '''User can click to view Dsr Master Data Report'''
    dsrmaster = DsrMasterData(page)
    dsrmaster.viewReport()

def test_closeDsrMasterData(page):
    '''Dsr Master Data Report loads sucessfully'''
    dsrmaster = DsrMasterData(page)
    dsrmaster.closeReport()
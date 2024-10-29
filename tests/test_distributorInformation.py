from models.main import LoginPage
from models.masterDataReports import DistributorInformation

def test_findDistributorInformation(page):
    '''User can navigate to Distributor Information Report'''
    user = DistributorInformation(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    user.findMasterDataReport()
    
def test_navDistributorInformation(page):
    '''User can navigate to Distributor Information report and select filters'''
    user = DistributorInformation(page)
    user.clickReport()
    
def test_viewDistributorInformation(page):
    '''User can click to view Distributor Information Report'''
    user = DistributorInformation(page)
    user.viewReport()

def test_closeDistributorInformation(page):
    '''Distributor Information Report loads sucessfully'''
    user = DistributorInformation(page)
    user.closeReport()
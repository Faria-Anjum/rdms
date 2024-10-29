from models.main import LoginPage
from models.masterDataReports import UserManagement

def test_findUserManagement(page):
    '''User can navigate to User Management Report'''
    user = UserManagement(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    user.findMasterDataReport()
    
def test_navUserManagement(page):
    '''User can navigate to User Management report and select filters'''
    user = UserManagement(page)
    user.clickReport()
    
def test_viewUserManagement(page):
    '''User can click to view User Management Report'''
    user = UserManagement(page)
    user.viewReport()

def test_closeUserManagement(page):
    '''User Management Report loads sucessfully'''
    user = UserManagement(page)
    user.closeReport()
from models.main import LoginPage
from models.masterDataReports import UserManagement
    
def test_navUserManagement(page):
    '''User can navigate to User Management Report and select filters'''
    user = UserManagement(page)
    user.findMasterDataReport()
    user.clickReport()
    
def test_viewUserManagement(page):
    '''User can click to view User Management Report'''
    user = UserManagement(page)
    user.viewReport()

def test_closeUserManagement(page):
    '''User Management Report loads sucessfully'''
    user = UserManagement(page)
    user.closeReport()
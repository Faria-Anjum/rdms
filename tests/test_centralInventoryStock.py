from models.main import LoginPage
from models.deviceReports import CentralInventoryStock

def test_findCentralInventoryStock(page):
    '''User can navigate to Central Inventory Stock Report'''
    inventory = CentralInventoryStock(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    inventory.findDeviceReports()
    
def test_navCentralInventoryStock(page):
    '''User can navigate to Central Inventory Stock Report'''
    inventory = CentralInventoryStock(page)
    inventory.clickReport()

def test_viewCentralInventoryStock(page):
    '''User can click to view Central Inventory Stock Report'''
    inventory = CentralInventoryStock(page)
    inventory.viewReport()

def test_closeCentralInventoryStock(page):
    '''Central Inventory Stock Report loads sucessfully'''
    inventory = CentralInventoryStock(page)
    inventory.closeReport()
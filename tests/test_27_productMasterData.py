from models.main import LoginPage
from models.masterDataReports import ProductMasterData
    
def test_navProductMasterData(page):
    '''User can navigate to Product Master Data Report and select filters'''
    productmaster = ProductMasterData(page)
    productmaster.clickReport()
    
def test_viewProductMasterData(page):
    '''User can click to view Product Master Data Report'''
    productmaster = ProductMasterData(page)
    productmaster.viewReport()

def test_closeProductMasterData(page):
    '''Product Master Data Report loads sucessfully'''
    productmaster = ProductMasterData(page)
    productmaster.closeReport()
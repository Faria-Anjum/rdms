from models.main import LoginPage
from models.reports import SimStock
    
def test_navSimStockReport(page):
    '''User can navigate to Sim Stock report and select filters'''
    sim = SimStock(page)
    sim.clickReport()
    
# def test_dateSimStockReport(page, today):
#     '''Date fields contain today's date in Sim Stock Report'''
#     sim = SimStock(page)
#     sim.isDateFilled(today)

def test_enterDate(page, twomonths):
    '''User can enter date range for Sim Stock Report'''
    sim = SimStock(page)
    sim.enterDateFrom(twomonths)
    
def test_viewSimStockReport(page):
    '''User can click to view Sim Stock Report'''
    sim = SimStock(page)
    #pytest.xfail(Sim.viewReport())
    sim.viewReport()

def test_closeSimStockReport(page):
    '''Sim Stock Report loads sucessfully'''
    sim = SimStock(page)
    sim.closeReport()
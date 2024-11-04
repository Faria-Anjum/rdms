from models.main import LoginPage
from models.reports import ScStock
import pytest

def test_navScStockReport(page):
    '''User can navigate to SC Stock report and select filters'''
    sc = ScStock(page)
    sc.clickReport()
    
# def test_dateScStockReport(page, today):
#     '''Date fields contain today's date in SC Stock Report'''
#     sc = ScStock(page)
#     sc.isDateFilled(today)

def test_enterDate(page, onemonth):
    '''User can enter date range for SC Stock Report'''
    sc = ScStock(page)
    sc.enterDateFrom(onemonth)
    
def test_viewScStockReport(page):
    '''User views SC Stock Report'''
    sc = ScStock(page)
    sc.viewReport()

def test_noScStockReport(page):
    '''User receives "No Data Found" error'''
    sc = ScStock(page)
    sc.noDataFound()
    
# def test_closeScStockReport(page):
#     '''SC Stock Report loads successfully'''
#     sc = ScStock(page)
#     sc.closeReport()
from models.main import LoginPage
from models.reports import SoPayment
import pytest

xfail = pytest.mark.xfail

def test_navSoPaymentReport(page):
    '''User can navigate to SO Payment Report and select filters'''
    so = SoPayment(page)
    so.findReport()
    so.clickSoReport()
    
# def test_dateSoPaymentReport(page, today):
#     '''Date fields contain today's date in SO Payment Report'''
#     so = SoPayment(page)
#     so.isDateFilled(today)

def test_enterDate(page, onemonth):
    '''User can enter date range for SO Payment Report'''
    so = SoPayment(page)
    so.enterDateFrom(onemonth)
    
def test_viewSoPaymentReport(page):
    '''User views SO Payment Report'''
    so = SoPayment(page)
    so.viewReport()
    
#@xfail
def test_noSoPaymentReport(page):
    '''User receives "No Data Found" error'''
    so = SoPayment(page)
    so.noDataFound()
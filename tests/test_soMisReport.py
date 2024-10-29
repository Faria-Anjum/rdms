from models.main import LoginPage
from models.reports import SoMisReport
import pytest

xfail = pytest.mark.xfail

def test_findSoMisReport(page):
    # context = browser.new_context(storage_state='auth.json')
    # page = context.new_page()

    '''User can view SO MIS Report tab'''
    so = SoMisReport(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    so.findReport()

def test_navSoMisReport(page):
    '''User can navigate to SO MIS report and select filters'''
    so = SoMisReport(page)
    so.clickSoReport()
    
def test_dateSoMisReport(page, today):
    '''Date fields contain today's date in SO MIS Report'''
    so = SoMisReport(page)
    so.isDateFilled(today)

def test_enterDate(page, onemonth):
    '''User can enter date range for SO MIS Report'''
    so = SoMisReport(page)
    so.enterDateFrom(onemonth)
    
def test_viewSoMisReport(page):
    '''User views SO MIS Report'''
    so = SoMisReport(page)
    so.viewReport()
    
@xfail
def test_noSoMisReport(page):
    '''User receives "No Data Found" error'''
    so = SoMisReport(page)
    so.noDataFound()
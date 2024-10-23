from models.main import LoginPage, SoMisReport
import pytest

xfail = pytest.mark.xfail

def test_findSoMisReportReport(page):
    # context = browser.new_context(storage_state='auth.json')
    # page = context.new_page()

    '''User can view SO MIS Report tab'''
    so = SoMisReport(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    so.findReport()

def test_navSoMisReportReport(page):
    '''User can navigate to SO MIS report and select filters'''
    so = SoMisReport(page)
    so.clickSoReport()
    
def test_dateSoMisReportReport(page):
    '''Date fields contain today's date in SO MIS Report'''
    so = SoMisReport(page)
    so.isDateFilled()

def test_enterDate(page):
    '''User can enter date range for SO MIS Report'''
    so = SoMisReport(page)
    so.enterDateFrom()
    
def test_viewSoMisReportReport(page):
    '''User views SO MIS Report'''
    so = SoMisReport(page)
    so.viewReport()
    
@xfail
def test_noSoMisReportReport(page):
    '''User receives "No Data Found" error'''
    so = SoMisReport(page)
    so.noDataFound()
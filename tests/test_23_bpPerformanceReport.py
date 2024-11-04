from models.main import LoginPage
from models.reports import BPPerformance
    
def test_navBpPerformanceReport(page):
    '''User can navigate to BP Performance Report and select filters'''
    bpperform = BPPerformance(page)
    bpperform.clickReport()

def test_enterDate(page, today, onemonth):
    '''User can enter date range for BP Performance Report'''
    bpperform = BPPerformance(page)
    bpperform.enterDateFromTo(today, onemonth)
    
def test_viewBpPerformanceReport(page):
    '''User can click to view BP Performance Report'''
    bpperform = BPPerformance(page)
    bpperform.viewReport()

def test_closeBpPerformanceReport(page):
    '''BP Performance Report loads sucessfully'''
    bpperform = BPPerformance(page)
    bpperform.closeReport()
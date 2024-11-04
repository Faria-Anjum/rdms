from models.main import LoginPage
from models.reports import DeliverySummary
    
def test_navDeliveryReport(page):
    '''User can navigate to Delivery Report Summary and select filters'''
    delivery = DeliverySummary(page)
    delivery.clickReport()

def test_enterDate(page, today, onemonth):
    '''User can enter date range for Delivery Report Summary'''
    delivery = DeliverySummary(page)
    delivery.enterDateFromTo(today, onemonth)
    
def test_viewDeliveryReport(page):
    '''User can click to view Delivery Report Summary'''
    delivery = DeliverySummary(page)
    delivery.viewReport()

def test_closeDeliveryReport(page):
    '''Delivery Report Summary loads sucessfully'''
    delivery = DeliverySummary(page)
    delivery.closeReport()
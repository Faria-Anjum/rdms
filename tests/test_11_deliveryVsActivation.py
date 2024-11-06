from models.main import LoginPage
from models.reports import DeliveryVsActivation
    
def test_navDeliveryVsActivationReport(page):
    '''User can navigate to Delivery vs Activation Summary Report and select filters'''
    delvsactiv = DeliveryVsActivation(page)
    delvsactiv.clickReport()

def test_enterDate(page, today, onemonth):
    '''User can enter date range for Delivery vs Activation Summary Report'''
    delvsactiv = DeliveryVsActivation(page)
    delvsactiv.enterDateFromTo(today, onemonth)
    delvsactiv.enterSecondDateFromTo(today, onemonth)
    
def test_viewDeliveryVsActivationReport(page):
    '''User can click to view Delivery vs Activation Summary Report'''
    delvsactiv = DeliveryVsActivation(page)
    delvsactiv.viewReport()

def test_closeDeliveryVsActivationReport(page):
    '''Delivery vs Activation Summary Report loads sucessfully'''
    delvsactiv = DeliveryVsActivation(page)
    delvsactiv.closeReport()
from models.main import LoginPage, DeliverySummary

def test_findDeliveryReport(page):
    '''User can navigate to Delivery Report Summary'''
    delivery = DeliverySummary(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    delivery.findReport()
    
def test_navDeliveryReport(page):
    '''User can navigate to Delivery Report Summary and select filters'''
    delivery = DeliverySummary(page)
    delivery.clickReport()

def test_enterDate(page):
    '''User can enter date range for Delivery Report Summary'''
    delivery = DeliverySummary(page)
    delivery.enterDateFromTo()
    
def test_viewDeliveryReport(page):
    '''User can click to view Delivery Report Summary'''
    delivery = DeliverySummary(page)
    delivery.viewReport()

def test_closeDeliveryReport(page):
    '''Delivery Report Summary loads sucessfully'''
    delivery = DeliverySummary(page)
    delivery.closeReport()
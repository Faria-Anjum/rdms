from models.main import LoginPage, DeliveryDetails

def test_findDeliveryReport(page):
    '''User can navigate to Delivery Report Details'''
    delivery = DeliveryDetails(page)
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    delivery.findReport()
    
def test_navDeliveryReport(page):
    '''User can navigate to Delivery Report Details and select filters'''
    delivery = DeliveryDetails(page)
    delivery.clickReport()

def test_enterDate(page):
    '''User can enter date range for Delivery Report Details'''
    delivery = DeliveryDetails(page)
    delivery.enterDateFromTo()
    
def test_viewDeliveryReport(page):
    '''User can click to view Delivery Report Details'''
    delivery = DeliveryDetails(page)
    delivery.viewReport()

def test_closeDeliveryReport(page):
    '''Delivery Report Details loads sucessfully'''
    delivery = DeliveryDetails(page)
    delivery.closeReport()
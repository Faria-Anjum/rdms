from models.main import LoginPage
from models.reports import BPTaggedList
    
def test_navBpTaggedList(page):
    '''User can navigate to BP Tagged List and select filters'''
    bptagged = BPTaggedList(page)
    bptagged.clickReport()
    
def test_viewBpTaggedList(page):
    '''User can click to view BP Tagged List'''
    bptagged = BPTaggedList(page)
    bptagged.viewReport()

def test_closeBpTaggedList(page):
    '''BP Tagged List loads sucessfully'''
    bptagged = BPTaggedList(page)
    bptagged.closeReport()
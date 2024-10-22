from models.main import LoginPage

def test_navigateLogin(page):
    '''User can navigate to login page'''
    login = LoginPage(page)
    login.navigate()

def test_enterCredentials(page, context):
    '''User can enter username and password'''
    login = LoginPage(page)
    login.loginCreds()
    storage=context.storage_state(path='auth.json')

def test_login(page):
    '''User can sign in to dashboard'''
    login = LoginPage(page)
    login.confirmSignIn()
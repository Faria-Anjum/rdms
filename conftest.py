import pytest
from datetime import datetime
import os

#all test functions in a test file run on the same browser context
@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    return page

#customizing html report
def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    #cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')

def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")
    #cells.insert(1, f'<td class="col-time">{datetime.now()}</td>')

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

#date range functions
@pytest.fixture(scope="session")
def today():
    today = datetime.now()

    year = today.year
    month = today.month
    day = today.day

    if len(str(today.day))==1:
        day = "0"+str(day)
    if len(str(today.month))==1:
        month = "0"+str(month)

    day = f'{year}-{month}-{day}'
    return day

@pytest.fixture(scope="session")
def onemonth():
    today = datetime.now()
    
    if today.month == 1:
        month = 12
        year = today.year - 1
    else:
        month = today.month - 1
        year = today.year

    if today.day in [28,29,30,31]:
        day = 1
        month = today.month
        year = today.year
    else:
        day = today.day + 1

    if len(str(day))==1:
        day = "0"+str(day)
    if len(str(month))==1:
        month = "0"+str(month)

    onemonth = f'{year}-{month}-{day}'
    return onemonth

@pytest.fixture(scope="session")
def twomonths():
    today = datetime.now()
    
    if today.month == 1:
        month = 11
        year = today.year - 1
    elif today.month == 2:
        month = 12
        year = today.year - 1
    else:
        month = today.month - 2
        year = today.year

    if today.day in [28,29,30,31]:
        day = 1
        month = today.month - 1
        year = today.year
    else:
        day = today.day

    if len(str(day))==1:
        day = "0"+str(day)
    if len(str(month))==1:
        month = "0"+str(month)

    twomonths = f'{year}-{month}-{day}'
    return twomonths

@pytest.fixture(scope="session")
def twoyears():
    today = datetime.now()
    
    year = today.year-2
    month = today.month
    day = today.day

    if len(str(today.day))==1:
        day = "0"+str(day)
    if len(str(today.month))==1:
        month = "0"+str(month)

    twoyears = f'{year}-{month}-{day}'
    return twoyears

#setting viewport
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

# Get session storage and store as env variable
# @pytest.fixture(scope="session")
# def storage(context):
#     session_storage = page.evaluate("() => JSON.stringify(sessionStorage)")
#     os.environ["SESSION_STORAGE"] = session_storage

#     # Set session storage in a new context
#     session_storage = os.environ["SESSION_STORAGE"]
#     context.add_init_script("""(storage => {
#     if (window.location.hostname === 'https://stage-dms.robi.com.bd/#/login') {
#         const entries = JSON.parse(storage)
#         for (const [key, value] of Object.entries(entries)) {
#         window.sessionStorage.setItem(key, value)
#         }
#     }
#     })('""" + session_storage + "')")

# def browser_context_args(browser_context_args):
#     return {
#     **browser_context_args,
#     "storage_state": "auth.json",
#     }
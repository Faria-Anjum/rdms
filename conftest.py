import pytest
from datetime import datetime
import os

# Get session storage and store as env variable
@pytest.fixture(scope="module")
def storage(context):
    session_storage = page.evaluate("() => JSON.stringify(sessionStorage)")
    os.environ["SESSION_STORAGE"] = session_storage

    # Set session storage in a new context
    session_storage = os.environ["SESSION_STORAGE"]
    context.add_init_script("""(storage => {
    if (window.location.hostname === 'example.com') {
        const entries = JSON.parse(storage)
        for (const [key, value] of Object.entries(entries)) {
        window.sessionStorage.setItem(key, value)
        }
    }
    })('""" + session_storage + "')")


#all test functions in a test file run on the same browser context
@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    return page

# def browser_context_args(browser_context_args):
#     return {
#     **browser_context_args,
#     "storage_state": "auth.json",
#     }

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
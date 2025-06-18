from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

def get_browserstack_driver(browser, os_name, os_version, username, access_key):
    options = Options()

    # Set up BrowserStack capabilities for OS, browser, etc.
    bstack_options = {
        'os': os_name,
        'osVersion': os_version,
        'sessionName': 'El Pais Selenium Test',  # Useful to identify this run in dashboard
        'buildName': 'El Pais Build 1',          # Group runs under the same build
        'debug': 'true'                          # Enables screenshots and logs
    }

    # Attach capabilities to options
    options.set_capability('browserName', browser)
    options.set_capability('bstack:options', bstack_options)

    # Build the BrowserStack remote URL with credentials
    url = f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub"

    # Return the Remote WebDriver instance that connects to BrowserStack
    return Remote(command_executor=url, options=options)

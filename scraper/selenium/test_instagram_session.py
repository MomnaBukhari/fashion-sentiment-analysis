# .............................................
# Experiment 002
# Verify Instagram session using Selenium
# .............................................
# This script is doing 4 actions:
# .. Open Chrome automation profile
# .. Open Instagram
# .. Verify login session
# .. Close browser
# .............................................



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



# .............................................
# configure Chrome options
options = Options()
options.add_argument(
r"--user-data-dir=C:\ChromeAutomation"
)
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options) # create browser session
# .............................................



# .............................................
# open Instagram
driver.get("https://www.instagram.com") # open Instagram
time.sleep(10) # wait for page to load
print("Instagram session opened successfully.")
input("Press ENTER to close browser...") # keep browser open for inspection
driver.quit() # close browser
# .............................................



# .............................................
# Summary
# selenium: browser automation library.
# webdriver: creates browser session.
# Options: configures Chrome startup settings.
# Profile: C:\ChromeAutomation
# Purpose: Verify Instagram remains logged in.
# Expected Result: Instagram opens without asking for login (should be already logged in).
# .............................................
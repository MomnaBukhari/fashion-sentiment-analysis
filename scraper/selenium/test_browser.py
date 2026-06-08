# .............................................
# Experiment 001
# Verify Selenium browser automation
# .............................................
# This script is doing 3 actions:
# .. Open Chrome browser
# .. Open Google homepage
# .. Close browser
# .............................................



from selenium import webdriver
import time



# .............................................
driver = webdriver.Chrome() # start browser session
driver.get("https://www.google.com") # open test website
time.sleep(5) # wait for visual verification
driver.quit() # close browser
# .............................................



# .............................................
# Summary
# selenium: browser automation library.
# webdriver: creates Chrome browser session.
# Purpose: Verify Selenium installation works.
# Expected Result: 
# .. Chrome opens successfully.
# .. Google homepage loads.
# .. Browser closes without errors.
# .............................................

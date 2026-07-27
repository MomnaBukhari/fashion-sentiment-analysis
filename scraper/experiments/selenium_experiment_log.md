# Experiment Log

## Experiment 001
Name:
Selenium Browser Test

Goal:
Verify Selenium installation and browser automation.

Result:
SUCCESS

Notes:
Chrome opened successfully.
Google homepage loaded.
Browser closed correctly.


## Experiment 002
Name:
Instagram Session Verification

Goal:
Verify Selenium can access Instagram using automation profile.

Result:
SUCCESS

Notes:
Chrome automation profile created.
Instagram session loaded successfully.
No login required as it should be previously logged in after profile creation.


## Experiment 003
Name:
Instagram Hashtag Scraping

Goal:
Collect Instagram posts from hashtag pages and extract textual metadata.

Result:
PARTIAL SUCCESS

Output:
data/raw/ootd_posts_full.json

Notes:
Successfully navigated to the Instagram hashtag page.
Successfully collected the first 10 post URLs.
Successfully visited each collected post.
Successfully generated a structured JSON output file.
Post caption and username extraction was not reliable because Instagram's dynamic page structure prevented the Selenium selectors from consistently locating the required elements.
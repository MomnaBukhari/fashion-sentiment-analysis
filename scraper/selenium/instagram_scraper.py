# .............................................
# Experiment 003
# Instagram hashtag scraping using Selenium
# .............................................
# Status: Final stage (textual post dataset extraction)
# Goal:
# .. Open Instagram hashtag page
# .. Collect post URLs
# .. Visit each post
# .. Extract textual metadata
# .. Save structured dataset
# .............................................



import os
import json
import time
import tkinter as tk
from tkinter import messagebox

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



# .............................................
# load environment variables
# .............................................
load_dotenv()

CHROME_PROFILE_PATH = os.getenv("CHROME_PROFILE_PATH", r"C:\ChromeAutomation")
HASHTAG = os.getenv("TARGET_HASHTAG_01", "ootd")
LIMIT = 10



# .............................................
# setup chrome options
# .............................................
options = Options()
options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")



# .............................................
# start browser
# .............................................
driver = webdriver.Chrome(options=options)



# .............................................
# open hashtag page
# .............................................
base_url = f"https://www.instagram.com/explore/tags/{HASHTAG}/"
driver.get(base_url)

time.sleep(8)



# .............................................
# collect post links
# .............................................
post_links = set()
scroll_attempts = 0
MAX_SCROLLS = 8

while len(post_links) < LIMIT and scroll_attempts < MAX_SCROLLS:

    anchors = driver.find_elements(By.TAG_NAME, "a")

    for a in anchors:
        href = a.get_attribute("href")

        if href and "/p/" in href:
            post_links.add(href)

        if len(post_links) >= LIMIT:
            break

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    scroll_attempts += 1


# .............................................
# visit each post and extract data (FIXED VERSION)
# .............................................

dataset = []

for idx, url in enumerate(list(post_links)[:LIMIT]):

    try:
        driver.get(url)
        time.sleep(6)  # allow full render

        # .............................................
        # extract username (more stable)
        # .............................................
        try:
            username = driver.find_element(
                By.XPATH,
                "//header//a[contains(@href,'/')]"
            ).text
        except:
            username = None


        # .............................................
        # extract caption (more reliable container)
        # .............................................
        try:
            caption_elements = driver.find_elements(
                By.XPATH,
                "//div[@role='presentation']//span"
            )

            caption = None

            for el in caption_elements:
                text = el.text
                if text and len(text) > 10:
                    caption = text
                    break

        except:
            caption = None


        dataset.append({
            "post_url": url,
            "caption": caption,
            "username": username
        })

        print(f"[{idx+1}/{LIMIT}] extracted")

    except Exception as e:
        print(f"Skipped post: {e}")
# .............................................



# save dataset
# .............................................
os.makedirs("data/raw", exist_ok=True)

output_file = "data/raw/ootd_posts_full.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=4, ensure_ascii=False)



print(f"Dataset saved: {output_file}")



# .............................................
# browser cleanup
# .............................................
driver.quit()



# .............................................
# completion popup (important feedback)
# .............................................
root = tk.Tk()
root.withdraw()

messagebox.showinfo(
    "Experiment 003 Complete",
    f"Scraping finished successfully.\n\nPosts collected: {len(dataset)}\nFile saved: {output_file}"
)


# .............................................
# Summary
# selenium: automates Chrome browser interactions.
# webdriver: creates and controls the Chrome browser session.
# dotenv: loads environment variables from the .env file.
# json: saves extracted data into JSON format.
# tkinter: displays a completion notification window.
#
# Output:
# data/raw/ootd_posts_full.json
#
# Expected Result:
# .. Open Instagram hashtag page.
# .. Collect first 10 post URLs.
# .. Visit each collected post.
# .. Save extracted data into a JSON dataset.
#
# Actual Result:
# .. Successfully opened Instagram hashtag page.
# .. Successfully collected post URLs.
# .. Successfully visited individual posts.
# .. Successfully created JSON output file.
# .. Caption and username extraction did not reliably return the required data because Instagram's dynamic page structure prevented the Selenium selectors from consistently locating the correct elements.
#
# Status:
# Partial Success
# Link collection works correctly.
# Post content extraction requires a more reliable extraction strategy.
# .............................................
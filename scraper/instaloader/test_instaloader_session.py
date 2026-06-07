# .............................................
# Experiment 001
# Verify Instaloader session loading
# .............................................



import os
import instaloader
from dotenv import load_dotenv



# .............................................
# load environment variables from .env file
load_dotenv()
instagram_username = os.getenv("INSTAGRAM_USERNAME") # load username from environment variable
# verify username exists
if not instagram_username:
    raise ValueError(
        "INSTAGRAM_USERNAME not found in .env file."
    )
print("Instagram username:", instagram_username)
# .............................................



# .............................................
instagram_loader = instaloader.Instaloader() # create Instaloader object
# load saved Instagram session
instagram_loader.load_session_from_file(
    instagram_username
)
print("Session loaded successfully.") # print confirmation message
# .............................................



# .............................................
# Summary
# os: Reads environment variables from the system.
# instaloader: Connects to Instagram and downloads public data.
# dotenv: Loads variables from .env file into Python.
# Experiment Purpose: Verify that Instagram authentication works.
# .............................................
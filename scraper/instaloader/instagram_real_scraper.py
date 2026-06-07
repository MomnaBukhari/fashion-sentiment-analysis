# .............................................
# Experiment 002
# Collect Instagram hashtag posts
# .............................................
# This script is doing 4 actions:
# .. Connect to Instagram hashtag data
# .. Extract posts one by one
# .. Convert into structured dataset (JSON)
# .. Save for preprocessing stage
# .............................................



import os
import json
import instaloader
from dotenv import load_dotenv


# .............................................
# load environment variables
load_dotenv()
instagram_username = os.getenv("INSTAGRAM_USERNAME") # load username from environment variable
# verify username exists
if not instagram_username:
    raise ValueError(
        "INSTAGRAM_USERNAME not found in .env file."
    )
# .............................................



# .............................................
# create Instaloader object
instagram_loader = instaloader.Instaloader()  # create Instaloader object
# load saved Instagram session
instagram_loader.load_session_from_file(instagram_username)
# .............................................



# .............................................
# define scraping settings
target_hashtag = "ootd"  # target Instagram hashtag
post_limit = 10          # maximum posts to collect
# .............................................



# .............................................
# collect hashtag posts
def scrape_hashtag():
    print(f"Collecting Instagram posts for #{target_hashtag}")
    collected_posts = []
    hashtag = instaloader.Hashtag.from_name(
        instagram_loader.context,
        target_hashtag
    )
    collected_count = 0
    for post in hashtag.get_posts():
        if collected_count >= post_limit:
            break
        try:
            collected_posts.append({
                "post_id": post.shortcode,
                "caption": post.caption,
                "hashtags": list(post.caption_hashtags),
                "likes": post.likes,
                "comments": post.comments,
                "date": str(post.date),
                "username": post.owner_username
            })
            collected_count += 1
            print(f"Collected post {collected_count}")
        except Exception as error:
            print(f"Skipped post: {error}")

    # save collected data in the file that will be created in the next step
    with open("data/raw/instagram_real.json", "w", encoding="utf-8") as json_file:
        json.dump(
            collected_posts,
            json_file,
            indent=4,
            ensure_ascii=False
        )
    print("Dataset saved to data/raw/instagram_real.json")
# .............................................



# .............................................
# run script
if __name__ == "__main__":
    scrape_hashtag()
# .............................................



# .............................................
# Summary
# os: reads environment variables securely
# json: saves structured data into JSON format
# instaloader: extracts Instagram public data
# dotenv: loads variables from .env file
#
# Output:
# data/raw/instagram_real.json
#
# Status:
# authentication works
# hashtag scraping currently blocked (Instagram restriction)
# Limitation: Instagram blocks hashtag endpoint for authenticated sessions via Instaloader API.
# .............................................
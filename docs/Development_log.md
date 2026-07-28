# --------- Phase 1 - Data Collection --------- 

# ---- For now I am using synthetic data. -----
A synthetic dataset that mimics Selenium + BeautifulSoup output with
- 500 multilingual posts
- duplicates
- missing captions
- emojis
- multiple languages
- URLs
- realistic metadata

# columnns collected:
- "post_id": "", ---------------------------------- NOt Useful - Unique identifier -----
- "platform": "", ---------------------------------     Useful -  Tells Data source
- "username": "", --------------------------------- NOt Useful - 
- "user_id": "", ---------------------------------- NOt Useful -  Unique account identifier
- "profile_verified": true, ----------------------- May Useful - 
- "profile_followers": 123, -----------------------     Useful - 
- "post_url": "", --------------------------------- NOt Useful -  
- "image_url": "", -------------------------------- NOt Useful -  
- "caption": "", ----------------------------------     Useful -  
- "hashtags": [], ---------------------------------     Useful -  
- "mentions": [ ----------------------------------- May Useful -  
        "abc"
    ],
- "language_hint": "", ----------------------------     Useful -  
- "location": "", ---------------------------------     Useful -  for EDA
- "fashion_category": "", ------------------------- May Useful -  
- "timestamp": "", --------------------------------     Useful -  
- "likes": 123, -----------------------------------     Useful -  
- "comments": 123, --------------------------------     Useful -  
- "scraped_at": "", ------------------------------- Not Useful -  
- "collection_method": "selenium_beautifulsoup" --- Not Useful -  

# Which columns will actually enter the model?
caption
language
sentiment
engagement
followers
fashion_category

.. The rest become metadata.

## Next
Start preprocessing.
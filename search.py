from googleapiclient.discovery import build
import os
import json
import unicodedata

my_api_key = os.environ['GOOGLE_API_KEY']
my_cse_id = os.environ['GOOGLE_CSE_ID']

def search(search_term):
    service = build("customsearch", "v1", developerKey=my_api_key)
    res = service.cse().list(q=search_term, cx=my_cse_id, num=1).execute()
    result = res['items']
    for result1 in result:
        title = str(result1['title'])
        snippet = str(result1['snippet'])
        
    message = unicodedata.normalize("NFKD", snippet)
    return message

    

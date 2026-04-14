import requests
import json
import time
from datetime import datetime
import os
#to create the path if not exists
if not os.path.exists('data'):
  os.makedirs("data")

url1 = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global", "police"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship", "cricket", "boxing", "tennis"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome", "chemistry", "nature", "years", "scientist", "climate"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming","anime"]
}

try:  #to handle the errors and execute code smoothly without crashing if the request fails
  response1=requests.get(url1, headers=headers)
  mylist = response1.json()
  print(len(mylist))
  if len(mylist) > 500: # to get exactl 500 valuesin the list
      mylist = mylist[500]
  else:
      print(f"The list only has {len(mylist)} items.")
except Exception as e:
  print(f"error fetching the data {e}")

all_trends=[] #empty list to add stories for each category

for category,keywords in categories.items():
  print(f"checking the category: {category}")
  count=0   
  for id in mylist:#looping through the ids 
    if count >=25: # to keep limit to 25 stories for each category to fetch stories from each "id"
      break
    url2= f"https://hacker-news.firebaseio.com/v0/item/{id}.json" # inserting "ids" to fetch the stories
    try:  #to handle the errors and execute code smoothly without crashing if the request fails
      response2 = requests.get(url2, headers=headers) # to fetch the data from the url
      if response2.status_code==200: # condition to execute onl if the request is successful
        data = response2.json() # geting data into json format
        title = data.get("title","").lower() #to avoid case sensitivity
        #fetches the words that matches with the words in title and exracts the info into the below objects
        if any(word in title for word in keywords): 
          extracted_item = {
                "post_id": data.get("id"),
                "title": data.get("title"),
                "category": category,
                "score": data.get("score"),
                "num_comments": data.get("descendants"),
                "author": data.get("by"),
                "collected_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                }
          all_trends.append(extracted_item) #appending all the the stories into the list
          count += 1 #to  increment the count for each iteration
          
      else:  #stops when request is failed for any id
        print(f"Request failed for ID {id}, moving on.")
    except Exception:
      print(f"Error connecting the id {id}")
      continue
  time.sleep(2) # waits for 2 sec after every category

date_str = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{date_str}.json"
with open(filename, 'w') as file: # creating a json file 
  json.dump(all_trends, file, indent=4)
print(f"Collected {len(all_trends)} stories. Saved to {filename}")
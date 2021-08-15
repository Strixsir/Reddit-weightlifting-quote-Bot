 # -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 13:58:48 2021

@author: strixsir
"""

import os
import re
from datetime import datetime
from replit import db
from keep_alive import keep_alive
import time
import praw
import csv
import random

with open("quotes.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)

reddit = praw.Reddit(
    client_id="k4UhQeTUiW4UWwpqC22wmA",
    client_secret="SPIerU5EX7w4b3RolvSZWWHvpeWRuQ",
    user_agent="Console:Happybot:1.0",
    username="bot1339",
    password="9an8ki7t",
    ratelimit_seconds=600
)

keep_alive()
sub=reddit.subreddit("myweightlosspics")
for com in sub.stream.comments():
        l=com.body
        l=l.strip()
        l=l.lower()
        listvar=l.split()
        if "quotebot" not in listvar:
          continue
        if not com.saved:
            rep=str(rows[random.randint(0,len(rows)-1)])
            com.save()
            com.reply(rep)
            
           
           
        
				

        
        
        
       
            
    
    

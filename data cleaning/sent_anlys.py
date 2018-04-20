#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 11:22:18 2018

@author: Jiaqi

"""
"""
install textblob

$ pip install -U textblob
$ python -m textblob.download_corpora
"""

from textblob import TextBlob

try:
    import json
except ImportError:
    import simplejson as json
def get_sent():
    tweets_filename = "3_25filtered.txt"
    tweets_file = open(tweets_filename, "r")
    tweet = json.loads(tweets_file.read()) 
    result=[]
    for item in tweet:
        text = item['data']['tweet']
        blob = TextBlob(text)
        result.append({
            'id':item['id'],
            'loc':item['data']['loc'],
            'sentiment':blob.sentiment.polarity

        })
    tweets_file.close
    return json.dumps(result)

if __name__ =="__main__":
    get_sent=get_sent()
    myfile = open("/Users/Jiaqi/Desktop/cse5559/sent_analysis/3_25sent.txt", "w")
    myfile.write(get_sent)
    myfile.close
    
    
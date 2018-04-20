#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 22:48:28 2018

@author: Jiaqi
"""

try:
    import json
except ImportError:
    import simplejson as json

    

def get_score(state,date):
    count=0
    score=0
    data_filename = "/Users/Jiaqi/Desktop/cse5559/sent_analysis/"+date+"sent.txt"
    data_file = open(data_filename, "r")
    data = json.loads(data_file.read())
    for item in data:
        if item['loc'][-2:]==state:
            count=count+1
            score=score+item['sentiment']
    if (count!=0):
        score=score/count
    else: 
        score=0
    return [state,date,count,score]

def data():
    states=[ "AK",
                      "AL",
                      "AR",
                      "AZ",
                      "CA",
                      "CO",
                      "CT",
                      "DE",
                      "FL",
                      "GA",
                      "HI",
                      "IA",
                      "ID",
                      "IL",
                      "IN",
                      "KS",
                      "KY",
                      "LA",
                      "MA",
                      "MD",
                      "ME",
                      "MI",
                      "MN",
                      "MO",
                      "MS",
                      "MT",
                      "NC",
                      "ND",
                      "NE",
                      "NH",
                      "NJ",
                      "NM",
                      "NV",
                      "NY",
                      "OH",
                      "OK",
                      "OR",
                      "PA",
                      "RI",
                      "SC",
                      "SD",
                      "TN",
                      "TX",
                      "UT",
                      "VA",
                      "VT",
                      "WA",
                      "WI",
                      "WV",
                      "WY"]
    dates=['3_3','3_4','3_5','3_6','3_7','3_8','3_9','3_15','3_17','3_18','3_19','3_21','3_23','3_24','3_25']
    result=[]
    for state in states:
        for date in dates:
            result.append(get_score(state,date))
    return result

def json_score(data):
    scores=[]
    for item in data:
        scores.append({
                'state':item[0],
                'date':item[1],
                'count':item[2],
                'score':item[3]
                })
    return json.dumps(scores)
    
    
if __name__ == "__main__":
    score=json_score(data())
    myfile = open("/Users/Jiaqi/Desktop/cse5559/sent_analysis/state_date_sent-more-more.txt", "w")
    myfile.write(score)
    myfile.close
    print()
    
    
    
        
    

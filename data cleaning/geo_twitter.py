#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:20:33 2018

@author: Jiaqi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:48:30 2018

@author: Jiaqi
"""


try:
    import json
except ImportError:
    import simplejson as json


##################################

#filter data
def run():
    tweets_filename = '/Users/Jiaqi/Desktop/cse5559/data/3_25.txt'
    tweets_file = open(tweets_filename, "r")
    data = []
    for line in tweets_file:
        tweet = json.loads(line)
        if ('place' in tweet) and (tweet['place']!=None):
                data.append({
                    'id':tweet['id'],
                    'data':{
                            'time':tweet['created_at'],
                            'loc':tweet['place']['full_name'],
                            'tweet':tweet['text'],
                    },
                    'lan':tweet['lang']
                })
    
    tweets_file.close

    return json.dumps(data)
                 

        

if __name__ == '__main__':
    result=run()
    myfile = open("3_25filtered.txt", "w")
    myfile.write(result)
    myfile.close


###############################









#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 13:44:54 2018

@author: Jiaqi
"""
import pandas as pd
import numpy
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
dates=["3/3/18","3/4/18","3/5/18","3/6/18","3/7/18","3/8/18","3/9/18","3/15/18","3/17/18","3/18/18","3/19/18","3/21/18","3/23/18","3/24/18"]




                    
#short = ["CA","TX","OH","GA","NY","IL","AK","AZ","FL","KY","MI","MN","MS","MO","NE","NV","NM","OR"];    
if __name__ == "__main__":
    #for state in states:
    #state = "CA" 
    #readfile(state)
    a = []

    for state in states:
        filename ="/Users/Jiaqi/Desktop/cse5559/weather data/raw/"+state+".csv"
        data=pd.read_csv(filename)
        
        for date in dates:
            weather = [[],[],[],[]]
            for index, row in data.iterrows():
                if row['DATE']==date:
                    weather[0].append(row['PRCP'])
                    weather[1].append(row['TAVG'])
    
                    weather[2].append(row['TMAX'])
                    weather[3].append(row['TMIN'])
            
            prc = numpy.nanmean(weather[0])
            tavg = numpy.nanmean(weather[1])
            tmax = numpy.nanmean(weather[2])
            tmin = numpy.nanmean(weather[3])
            a.append([date,state,prc,tavg,tmax,tmin])
       

    my_df = pd.DataFrame(a)
    headers=["date","state","PRC","AVGT","MAXT","MINT"]

    my_df.to_csv('my_csv.csv', index=False, header=headers)

    
    
    
    
    
    
    
    
    
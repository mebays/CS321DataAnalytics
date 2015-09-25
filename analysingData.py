#!/usr/bin python

import csv
import json
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import datetime
import re

def readingData():
    with open('new.csv') as openfile:
        reader = csv.DictReader(openfile)
        count = 0
        timeCounts = 1
        timeArray=[]
        timeFormat=[]
        temp= next(reader)
        tempTime = temp['created_utc']
        tempAuth = temp['author']
        timeFormat.append(datetime.datetime.fromtimestamp(int(tempTime)).strftime('%Y-%m-%d %H:%M:%S'))
       # maximum = len(reader[0])

        for row in reader:
            if (row['created_utc']==tempTime):
                timeCounts +=1
                count +=1
            else:
                tempTime = row['created_utc']
                timeArray.append(timeCounts)
                timeFormat.append(datetime.datetime.fromtimestamp(int(tempTime)).strftime('%Y-%m-%d %H:%M:%S'))
                #timeFormat.append(int(tempTime))
                timeCounts = 1
                count +=1
    
    if (len(timeArray) != len(timeFormat)):
        timeArray.append(timeCounts)
    return timeArray, timeFormat
'''
            time = datetime.datetime.fromtimestamp(int(row['created_utc'])).strftime('%Y-%m-%d')
            print time
            count +=1
            if count==500:
                break
'''

def dataResults():
    timeResults, timeFormat = readingData()
    maxResult = max(timeResults)
    minResult = min(timeResults)
    average = np.mean(timeResults)
    middle = np.median(timeResults)
    standardDev = np.std(timeResults)
    print maxResult
    print minResult
    print average
    print middle
    print standardDev
    print len(timeFormat)
    print "Total Data %s" % sum(timeResults)
    print "Total len of Time is %d seconds" %len(timeFormat)
    timeForFourhours=[]
    resultsForFourHours=[]
    for i in range(0, len(timeFormat), 3600):
        try:
            timeForFourhours.append(timeFormat[i]+'-'+timeFormat[i+3599])
            resultsForFourHours.append(sum(timeResults[i:i+3599]))
        except:
            break #skip the ending to make just 16 hours
    print timeForFourhours
    print resultsForFourHours
    maxResult = max(resultsForFourHours)
    minResult = min(resultsForFourHours)
    average = np.mean(resultsForFourHours)
    middle = np.median(resultsForFourHours)
    standardDev = np.std(resultsForFourHours)
    print maxResult
    print minResult
    print average
    print middle
    print standardDev
    print len(timeFormat)
    print "Total Data %s" % sum(timeResults)
    print "Total len of Time is %d seconds" %len(timeFormat)

    x = [i for i in range(len(timeForFourhours))]
    y = resultsForFourHours

    plt.plot(x, y, 'or')
    plt.axis([0, len(timeForFourhours), 0, max(resultsForFourHours)+10000])
        
    plt.show()
dataResults()



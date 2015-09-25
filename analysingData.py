#!/usr/bin python

import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime

from pylab import *

def readingDateData():
    with open('new.csv') as openfile:
        reader = csv.DictReader(openfile)
        timeCounts = 1
        timeArray=[]
        timeFormat=[]
        temp= next(reader)
        tempTime = temp['created_utc']
        timeFormat.append(datetime.datetime.fromtimestamp(int(tempTime)).strftime('%Y-%m-%d %H:%M'))

        for row in reader:
            if (row['created_utc']==tempTime):
                timeCounts +=1
            else:
                tempTime = row['created_utc']
                timeArray.append(timeCounts)
                timeFormat.append(datetime.datetime.fromtimestamp(int(tempTime)).strftime('%Y-%m-%d %H:%M'))
                timeCounts = 1
    
    if (len(timeArray) != len(timeFormat)):
        timeArray.append(timeCounts)

    return timeArray, timeFormat


def dateDataResults():
    timeResults, timeFormat = readingDateData()
    maxResult = max(timeResults)
    minResult = min(timeResults)
    average = np.mean(timeResults)
    middle = np.median(timeResults)
    standardDev = np.std(timeResults)
    print 'Max of the Results per second is %s' %maxResult
    print 'Min of the Results per second is %s' %minResult
    print 'Mean Result per second is %s' %average
    print 'Median Result per second is %s' %middle
    print 'Staandard deviation for seconds is %s' %standardDev
    print len(timeFormat)
    print "Total Data %s" % sum(timeResults)
    print "Total len of Time to obtain %d results is %d seconds" %(sum(timeResults),len(timeFormat))

    ##converstion from seconds to hours
    timeForFourhours=[]
    resultsForFourHours=[]
    for i in range(0, len(timeFormat), 3600+120):# To shift time to get closer per hour becaue some times ranges per second doesn't have a comment
        try:# try so make sure not going out of range
            timeForFourhours.append(timeFormat[i]+'-'+timeFormat[i+3599+120])
            resultsForFourHours.append(sum(timeResults[i:i+3599+120]))
        except:# break when out of range to cut off at an hour point
            break #skip the ending to make just 16 hours 
    print timeForFourhours
    print resultsForFourHours
    maxResult = max(resultsForFourHours)
    minResult = min(resultsForFourHours)
    average = np.mean(resultsForFourHours)
    middle = np.median(resultsForFourHours)
    standardDev = np.std(resultsForFourHours)
    print 'Max from Results per hour is %s' %maxResult
    print 'Min from Results per hour is %s' %minResult
    print 'Mean Result per hour %s' %average
    print 'Median Result per hour %s' %middle
    print 'Standard deviation for hours is %s' %standardDev
    print "Total Data %s" % sum(resultsForFourHours)
    print "Total len of Time is %d hours" %len(timeForFourhours)

    x = [i for i in range(len(timeForFourhours))]
    y = resultsForFourHours

    plt.plot(x, y, 'or')
    plt.axis([0, len(timeForFourhours), 0, max(resultsForFourHours)+10000])
    plt.xlabel(' Time gap in hours between Comments From 8:00 p.m. 7/31/15 to 12:00 p.m. 8/1/15')
    plt.ylabel('Number of comments')
    plt.title('Number of Comments vs Time Gap in Hours')
    plt.show()

    fig, ax = plt.subplots()
    rects1 = ax.bar(np.arange(16), resultsForFourHours, 0.5, color='g', yerr=standardDev)
    plt.xlabel(' Time gap in hours between Comments From 8:00 p.m. 7/31/15 to 12:00 p.m. 8/1/15')
    plt.ylabel('Number of comments')
    plt.title('Bar Graph for Comments Per Hour')
    plt.show()

    ##conversion for Fractions
    fractions=[]
    for i in range(0, len(resultsForFourHours)):
        fractions.append(round((float(resultsForFourHours[i])/(sum(resultsForFourHours))*100), 2))
    print fractions
    print sum(fractions)

    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    labels = timeForFourhours
    
    pie(fractions, labels=labels, autopct='%1.1f%%')
    title('Percentage in of Comments Per Hour')
    show()

def readingScoreData():
    with open('new.csv') as openfile:
        reader = csv.DictReader(openfile)
        count = 0 
        allScore = []
        positiveScore = []
        negativeScore = []
        zeroScore = []
        for row in reader:
            score = int(row['score'])
            allScore.append(score)
            if (score >0):
                positiveScore.append(score)
            elif(score < 0):
                negativeScore.append(score)
            else:
                zeroScore.append(score)

        print len(positiveScore)
        print len(negativeScore)
        print len(zeroScore)

    return allScore, positiveScore, negativeScore, zeroScore

def scoreDataResults():
    allScores, positiveScores, negativeScores, zeroScores = readingScoreData()
    totalNumber = len(allScores)
    maxScore = max(allScores)
    minScore = min(allScores)
    print "total number of data is %s" %totalNumber
    print "Maximum score is %s" %maxScore
    print "Minimum score is %s" %minScore
    meanScore = np.mean(allScores)
    medianScore = np.median(allScores)
    stdScore = np.std(allScores)
    print "Mean Score is %s" %meanScore
    print "Median Score is %s" %medianScore
    print "The standart Dev. is %s" %stdScore
    
    allDataGroupedWithTime=[]
    for i in range(0, len(allScores), 3600+120):# To shift time to get closer per hour becaue some times ranges per second doesn't have a comment
        try:# try so make sure not going out of range
            allDataGroupedWithTime.append(np.mean(allScores[i:i+3599+120]))
        except:# break when out of range to cut off at an hour point
            break #skip the ending to make just 16 hours 

    totalNumber = len(allDataGroupedWithTime)
    maxScore = max(allDataGroupedWithTime)
    minScore = min(allDataGroupedWithTime)
    print "total number of data is %s" %totalNumber
    print "Maximum score is %s" %maxScore
    print "Minimum score is %s" %minScore
    meanScore = np.mean(allDataGroupedWithTime)
    medianScore = np.median(allDataGroupedWithTime)
    stdScore = np.std(allDataGroupedWithTime)
    print "Mean Score is %s" %meanScore
    print "Median Score is %s" %medianScore
    print "The standart Dev. is %s" %stdScore

    print "\nPOSITIVE VALUE DATA \n\n"
    totalNumber = len(positiveScores)
    maxScore = max(positiveScores)
    minScore = min(positiveScores)
    print "total number of data is %s" %totalNumber
    print "Maximum score is %s" %maxScore
    print "Minimum score is %s" %minScore
    meanScore = np.mean(positiveScores)
    medianScore = np.median(positiveScores)
    stdScore = np.std(positiveScores)
    print "Mean Score is %s" %meanScore
    print "Median Score is %s" %medianScore
    print "The standart Dev. is %s" %stdScore

    print "\nNEGATIVE VALUE DATA \n\n"
    totalNumber = len(negativeScores)
    maxScore = max(negativeScores)
    minScore = min(negativeScores)
    print "total number of data is %s" %totalNumber
    print "Maximum score is %s" %maxScore
    print "Minimum score is %s" %minScore
    meanScore = np.mean(negativeScores)
    medianScore = np.median(negativeScores)
    stdScore = np.std(negativeScores)
    print "Mean Score is %s" %meanScore
    print "Median Score is %s" %medianScore
    print "The standart Dev. is %s" %stdScore

    print "\nZERO VALUE DATA \n\n"
    totalNumber = len(zeroScores)
    print "total number of data is %s" %totalNumber

    plt.plot(allScores)
    plt.xlabel("Score Count")
    plt.ylabel("Scores")
    plt.title("Score vs. Score Count")
    plt.show()

    plt.plot(positiveScores)
    plt.xlabel("Positive Score Count")
    plt.ylabel("Scores")
    plt.title("Score vs. Positive Score Count")
    plt.show()

    plt.plot(negativeScores)
    plt.xlabel("Negative Score Count")
    plt.ylabel("Scores")
    plt.title("Score vs Negative Score Count")
    plt.show()
    

    fractions=[]
    fractions.append((float(len(positiveScores))/len(allScores))*100)
    fractions.append((float(len(negativeScores))/len(allScores))*100)
    fractions.append((float(len(zeroScores))/len(allScores))*100)

    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    labels = ['positive','negative','zero']
    
    pie(fractions, labels=labels, autopct='%1.1f%%')
    title('Percentage of positive, negative, and zero Scores')
    show()


if __name__=='__main__':
    dateDataResults()
    scoreDataResults()

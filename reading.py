# vim: ts=8 et sw=4 sts=4

import csv
import json

def createCSV():
    with open('C:/Users/Matthew/Documents/CS321/RC_2015-08.csv', mode='r') as infile:
        reader = csv.reader(infile)
        print infile
        print reader
        with open('new.csv', mode = 'w') as outfile:
            writer = csv.writer(outfile, delimiter=' ', quotechar =',',quoting=csv.QUOTE_MINIMAL)
            count = 0
            for r in reader:
                if count == 1000000:
                    break
                writer.writerows(r)
                count +=1
        outfile.close()

    infile.close()
            

def readjson():
    with open('C:/users/matthew/documents/2015Fall/cs321/rc_2015-08.json', mode='r') as infile:
        with open('C:/users/matthew/documents/2015Fall/cs321/new.csv', mode = 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['body','gilded','subreddit_id', 'author_flair_css_class', 'edited','subreddit','author_flair_text','author', 'created_utc', 'distinguished','parent_id', 'score', 'retrieved_on','id','link_id','ups','controversiality'])
        
            for i in range(1000000):
                jdata =json.loads(infile.readline())
                try:
                    body = jdata['body'].encode('ascii','ignore')
                except:
                    body = 'Error'
                try:
                    gilded = jdata['gilded']
                except:
                    gilded = 'Error'
                try:
                    subreddit_id = jdata['subreddit_id']
                except:
                    subreddit_id = 'Error'
                try:
                    author_flair_css_class = jdata['author_flair_css_class']
                except:
                    author_flair_css_class = 'Error'
                try:
                    edited = jdata['edited']
                except:
                    edited = 'Error'
                try:
                    subreddit = jdata['subreddit']
                except:
                    subreddit = 'Error'
                try: 
                    author_flair_text = jdata['author_flair_text'].encode('ascii','ignore')
                except:
                    author_flair_text = 'Error'
                try:
                    author = jdata['author']
                except:
                    author = 'Error'
                try:
                    created_utc = jdata['created_utc']
                except:
                    created_utc = 'Error'
                try:
                    distinguished = jdata['distinguished']
                except:
                    distinguished = 'Error'
                try:
                    parent_id = jdata['parent_id']
                except:
                    parent_id = 'Error'
                try:
                    score = jdata['score']
                except:
                    score = 'Error'
                try:
                    retrieved_on = jdata['retrieved_on']
                except:
                    retrieved_on = 'Error'
                try:
                    _id = jdata['id']
                except:
                    _id = 'Error'
                try:
                    link_id = jdata['link_id']
                except:
                    link_id = 'Error'
                try:
                    ups = jdata['ups']
                except:
                    ups = 'Error'
                try:
                    controversiality = jdata['controversiality'].encode('ascii','ignore')
                except:
                    controversiality = 'Error'
                writer.writerow([body,
                                 gilded,
                                 subreddit_id,
                                 author_flair_css_class,
                                 edited,
                                 subreddit,
                                 author_flair_text,
                                 author,
                                 created_utc,
                                 distinguished,
                                 parent_id,
                                 score,
                                 retrieved_on,
                                 _id,
                                 link_id,
                                 ups,
                                 controversiality])           

readjson()

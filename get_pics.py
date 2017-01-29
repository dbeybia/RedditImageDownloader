#!/usr/bin/env python2
# encoding: utf-8


''''
A vert simple tool to grab images from a reddit subreddit.
I've seen alternatives to this, and I've also seen tools that gets the job done more nicely
but this is created for simplicity and minimalism, I wanted to create the simplest image downloader I can.

Baha  @dbeybia
'''

from __future__ import (absolute_import, division, print_function, unicode_literals)
import praw
import urllib
import gallery_get
import os



USERAGENT = 'Image downloader by /u/medtn'
SUBREDDIT = raw_input('Please enter the name of the subreddit: ')


def get_pics():
    '''
    Added a a get_pics function based on a suggestion form /u/schleifer
    '''
r = praw.Reddit(USERAGENT)
submissions = r.get_subreddit(SUBREDDIT).get_hot(limit=1000)
cwd = os.getcwd()

newpath = cwd + '\\images' 

if not os.path.exists(newpath):
    os.makedirs(newpath)

print ('Starting download for subreddit :', SUBREDDIT, '\n')

for submission in submissions:
	try:
		if 'imgur.com/a/' in submission.url: # launch the gallery_get module if this condition is true (if the link is an album)
				fullfilename = os.path.join(newpath, 'Picture - '+submission.id)
				print ('> ' + submission.url)
				gallery_get.run(submission.url)

		elif 'http://imgur.com/' in submission.url: # if the link is not a direct link (as in http://imgur.com/picture.jpg) a direct one will be appended to it
			fullfilename = os.path.join(newpath, submission.id + '.jpg')
			url = submission.url + '.jpg'
			print ('> * ' + url)
			urllib.urlretrieve(url, fullfilename)
		elif 'i.redd.it' in submission.url:
			fullfilename = os.path.join(newpath, submission.id+ '.jpg')

			url = submission.url
			print ('>  ' + url)
			urllib.urlretrieve(url, fullfilename)

		else: 
			fullfilename = os.path.join(newpath, submission.id+ '.jpg')

			urllib.urlretrieve(submission.url, fullfilename)
			print ('> ' + submission.url)
	except:
			pass



if __name__ == '__main__':
    if not USERAGENT:
        print('Missing useragent')
    elif not SUBREDDIT:
        print('Missing subreddit')
    else:
        get_pics()
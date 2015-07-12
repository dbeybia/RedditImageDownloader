# The simplest tool ever to grab images from a reddit subreddit.
#
# I've seen alternatives to this, and I've also seen tools get the job done more nicely
# but this is created for simplicity and minimalism, I wanted to create the simplest image download I can.
#
# Baha - meddbeibia@gmail.com - @meddbeibia
# JULY 12, 2015
import praw
import urllib
import gallery_get
import time

r = praw.Reddit(user_agent='An image downloader - meddbeibia@gmail.com')
submissions = r.get_subreddit('pics').get_hot(limit=25) # subreddit in this case is 'pics', you could change the subreddit (hopefully not to /r/gonewild)
														# You could also change the page limit (reddit allows up to 1000)

print '---------- Initializing download ----------'
time.sleep(1)
print '----------      Downloading      ----------'
print ('\n')
for submission in submissions:
   try:

	if "imgur.com/a/" in submission.url: # launch the gallery_get module if this condition is true (if the link is an album)
		print ("> " + submission.url)
		gallery_get.run(submission.url)

	elif "http://imgur.com/" in submission.url: # if the link is not a direct link (as in http://imgur.com/picture.jpg) a direct one will be appended to it
		#print submission.url
		url = submission.url + ".jpg"
		print ('> * ' + url)
		urllib.urlretrieve(url, "Picture - "+submission.id+".jpg")

	else: 
		urllib.urlretrieve(submission.url, "Picture - "+submission.id+".jpg")
		print ("> " + submission.url)
   except:
        pass
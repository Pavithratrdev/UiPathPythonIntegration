from twython import Twython
from better_profanity import profanity


profanity.load_censor_words()


# Define our constant variables, this is all the data we wrote down in the first part of the tutorial.
CONSUMER_KEY = 'NzVLUzzixbmU3irpzbhf9BZDd'  
CONSUMER_SECRET = 'XittN5A3WADNQRYScDOcndqdHlg5Jq0Lg5i5Bvpr0ElxoTgCxK'
ACCESS_KEY = '1428323567582670851-pg2AvGeUvH0UTPvgK8mtlnEszDT0M8'
ACCESS_SECRET = 'Ow0zvO8d56MfoIjfOfubPu3aTdIo5EtrErAB1rCXcYxYs'

# Create a copy of the Twython object with all our keys and secrets to allow easy commands.
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

def tweetPostMsg(msg):
    #Profanity Check
    censored_msg = profanity.censor(msg)

    if '*' not in censored_msg:
        api.update_status(status=msg)  
        #return "Good Comments" + msg
    else:
        return "Bad comments cannot be posted to social media." + censored_msg
    return "Comment Posted:" + msg
#print(tweetPostMsg("welcome3"))
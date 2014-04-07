'''
HeartFixBot by /u/ddNTP as requested by /u/godhand1942 @ http://www.reddit.com/r/botrequests/comments/22802i/request_a_bot_that_replaces_3_with/

If a user types 'I <3 you', HeartFixBot will reply with 'FTFY: I ♥ you'

'''

# D.O.B.
DOB = "6 April 2014"

# Version
version = "1.0.0"

# Internals
PRAW = "2.1.14"
Python = "3.3.5"

# Imports
import praw, time
from time import sleep

# User Agent
bot = praw.Reddit("HeartFixBot " + str(version) + " by /u/ddNTP")

# Track comment_id
done = set()


## START HERE ------------------------------------------------------------------------------------

t = 30    ## Initial sleep before bot begins

sub = 'planetside'    ## Subreddit to crawl

fixcount = 0

print ("Starting up HeartFixBot")

def login():
    username = input("Reddit username: ")    
    password = input("Reddit password: ")    
    bot.login(username, password)

loggedin = False
while not loggedin:
    try:
        timeset = time.strftime("%d/%m/%y %H:%M:%S")
        print(timeset + " Logging into Reddit...")
        login()
        loggedin = True
        print(timeset + " Login successful!")
    except praw.errors.InvalidUserPass:
        print ("Invalid username/password, please reauthenticate")

def init_sleep(t):
    print("Initial sleep for " + str(t) + " seconds.")
    for i in range(t, 0, -1):
        time.sleep(1)
        print (i)

init_sleep(t)

running = True
while running:
    try:
        count = 0   
        comments = bot.get_comments(sub, limit = 500)
        for comment in comments:
            count += 1        
            if ('I <3 you' in str(comment).lower()) and (comment.id not in done):
                done.add(comment.id)
                comment.reply('FTFY: I ♥ you')
                fixcount += 1
                with open("heartfixbot_comment_id.txt", "a") as outfile:
                    outfile.write(comment.id + " ")

                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " -FIXED " + str(fixcount) + " comments'-")
                print (done)
            else:
                pass
                              
        timeset = time.strftime("%d/%m/%y %H:%M:%S")
        print (timeset + " Just scanned " + str(count) + " comments.")
        sleep(60)
                             
    # ERROR # Exception as e: # praw.errors.RateLimitExceeded:
    except Exception as e:
        timeset = time.strftime("%d/%m/%y %H:%M:%S")
        print (timeset + " -ERROR- Rate limit exceeded.")
        sleep(300) # IF ERROR OCCURED, SLEEP FOR 300 SECONDS (5 MINS)

## FIN -----------------------------------------------------------------------------------------
        

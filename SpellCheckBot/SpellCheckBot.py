'''
SpellCheckBot by /u/ddNTP

[Python 3] SpellCheckBot is designed to search for comments on Reddit that have spelling mistakes...


-----------------------------------------------------------------------------------------------------------------------------------------------
    Banned from:                                    Reason:                                   Link:
-----------------------------------------------------------------------------------------------------------------------------------------------

/r/nfl              28 March 2014 @ ~18:40 PM       We don't allow novelty accounts           http://www.reddit.com/message/messages/1pl3bu
/r/funny            28 March 2014 @ ~19:01 PM       Bots aren't allowed in /r/funny           http://www.reddit.com/message/messages/1p8gq9
/r/leagueoflegends  28 March 2014 @ ~19:16 PM       We don't allow novelty bots               http://www.reddit.com/message/messages/1p8gww
/r/xboxone          31 March 2014 @ ~07:01 AM       We don't want junk bots                   http://www.reddit.com/message/messages/1pitsw

--------------------
       Stats:
--------------------

As of April 1 2014 09:32 PM PST
      
SpellCheckBot has sent out:
* 63 instances of should have         (search for should of)
* 50 instances of could have          (search for could of
* 73 instances of would have          (search for would of)

------------------------
       Milestones:
------------------------

1000 comment karma   April 2 2014 11:28 PM PST

'''

# D.O.B.
DOB = "March 24 2014"

# Version
version = "1.1.2"

# Internals
PRAW = "2.1.14"
Python = "3.3.5"

# Imports
import praw, time
from time import sleep

# User Agent
bot = praw.Reddit("SpellCheckBot " + str(version) + " by /u/ddNTP")

# Track comment_id of each spelling error
done1 = set()
done2 = set()
done3 = set()

# Record comment_id in a .txt file
def shouldhave_comment_id():
    with open("shouldhave_comment_id.txt", "wt") as out_file:
        for i in done1:
            out_file.write(i + " ")

def couldhave_comment_id():
    with open("couldhave_comment_id.txt", "wt") as out_file:
        for i in done2:
            out_file.write(i + " ")

def wouldhave_comment_id():
    with open("wouldhave_comment_id.txt", "wt") as out_file:
        for i in done3:
            out_file.write(i + " ")

## START HERE ----------------------------------------------------------------------------------------------------------------

t = 45    ## Initial sleep before bot runs
    
shouldhave = 0
couldhave = 0
wouldhave = 0
affectedme = 0

print("Starting up SpellCheckBot")

def login():
    username = input("Reddit username: ")    ### COMPLETE THIS
    password = input("Reddit password: ")    ### COMPLETE THIS
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
        # COUNTER
        count = 0 
        
        # SCAN COMMENTS
        comments = bot.get_comments('all', limit = 500)
        for comment in comments:
            count += 1
                        
            if ('should of ' in str(comment).lower()) and (comment.id not in done1):

                # REPLY TO COMMENT
                done1.add(comment.id)
                comment.reply('>*should have* \n >>**Example:** Gertrude is so fake, she should have two Facebook accounts. One for each face! \n >>> ^(Parent comment may have been edited/deleted.) ^(Help me help you improve in English!)')
                shouldhave += 1
                shouldhave_comment_id()

                # CONSOLE DEBUG
                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " ---FOUND A TOTAL OF " + str(shouldhave) + " people who use 'should of'---")
                print (done1)

            elif ('could of ' in str(comment).lower()) and (comment.id not in done2):
                
                done2.add(comment.id)
                comment.reply('>*could have* \n >>**Example:** If I could have just one dance with you, I would pick a song that never ends. \n >>> ^(Parent comment may have been edited/deleted.) ^(Help me help you improve in English!)')
                couldhave += 1
                couldhave_comment_id()

                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " ---FOUND A TOTAL OF " + str(couldhave) + " people who use 'could of'---")
                print (done2)

            elif ('would of ' in str(comment).lower()) and (comment.id not in done3):

                done3.add(comment.id)
                comment.reply('>*would have* \n >>**Example:** I would have gotten away with it too... meddling kids. \n >>> ^(Parent comment may have been edited/deleted.) ^(Help me help you improve in English!)')
                wouldhave += 1
                wouldhave_comment_id()

                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " ---FOUND A TOTAL OF " + str(wouldhave) + " people who use 'would of'---")
                print (done3)

            else:
                pass

        timeset = time.strftime("%d/%m/%y %H:%M:%S")
        print (timeset + " Just scanned " + str(count) + " comments.")
        sleep(60)
		
    # ERROR # Exception as e: # praw.errors.RateLimitExceeded:
    except Exception as e:
        timeset = time.strftime("%d/%m/%y %H:%M:%S")
        print (timeset + " --ERROR-- Rate limit exceeded.")
        sleep(300) # IF ERROR OCCURED, SLEEP FOR 300 SECONDS
                        

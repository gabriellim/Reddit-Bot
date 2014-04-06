'''
SpellCheckBot by /u/ddNTP

[Python 3] SpellCheckBot is designed to search for comments on Reddit that have spelling mistakes...


-----------------------------------------------------------------------------------------------------------------------------------------------
    Banned from:                                    Reason:                                   Link:
-----------------------------------------------------------------------------------------------------------------------------------------------

/r/nfl              28 March 2014 @ ~6:40  PM       We don't allow novelty accounts           http://www.reddit.com/message/messages/1pl3bu
/r/funny            28 March 2014 @ ~7:01  PM       Bots aren't allowed in /r/funny           http://www.reddit.com/message/messages/1p8gq9
/r/leagueoflegends  28 March 2014 @ ~7:16  PM       We don't allow novelty bots               http://www.reddit.com/message/messages/1p8gww
/r/xboxone          31 March 2014 @ ~7:01  AM       We don't want junk bots                   http://www.reddit.com/message/messages/1pitsw
/r/asoiaf            3 April 2014 @ ~12:31 PM       Pending reply                             http://www.reddit.com/message/messages/1pwd26
/r/relationships     6 April 2014 @ ~2:25  PM       Pending reply                             http://www.reddit.com/message/messages/1q8wyp


--------------------
       Stats:
--------------------

Since March 24 2014 8:30 PM PST
As of April 6 2014 4:13 PM PST
      
SpellCheckBot has sent out:
* 196 instances of should have          (search for should of)
* 132 instances of could have           (search for could of
* 230 instances of would have           (search for would of)
* 15   instances of must have           (search for must of)

------------------------
       Milestones:
------------------------

1000 comment karma   April 2 2014 11:28 PM PST

'''

# D.O.B.
DOB = "March 24 2014"

# Version
version = "1.1.6"

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
done4 = set()

## START HERE ----------------------------------------------------------------------------------------------------------------

t = 15    ## Initial sleep before bot runs
    
shouldhave = 0
couldhave = 0
wouldhave = 0
musthave = 0

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
                comment.reply('Homophone error detected. [What is it?](http://www.reddit.com/r/SpellingB/comments/22bwnw/homophone_error) \
                              \n **should have** \n *Example:* Two-Face should have created two Facebook accounts. One for each face! \
                              \n *** \n ^(Parent comment may have been edited/deleted.)')
                shouldhave += 1

                # RECORD comment.id
                with open("shouldhave_comment_id.txt", "a") as outfile:
                outfile.write(comment.id + " ")

                # CONSOLE DEBUG
                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " ---FOUND A TOTAL OF " + str(shouldhave) + " people who use 'should of'---")
                print (done1)

            elif ('could of ' in str(comment).lower()) and (comment.id not in done2):
                
                done2.add(comment.id)
                comment.reply('Homophone error detected. [What is it?](http://www.reddit.com/r/SpellingB/comments/22bwnw/homophone_error) \
                              \n **could have** \n *Example:* I could have taken the earlier train. \
                              \n *** \n ^(Parent comment may have been edited/deleted.)')
                couldhave += 1

                with open("couldhave_comment_id.txt", "a") as outfile:
                outfile.write(comment.id + " ")
        
                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " ---FOUND A TOTAL OF " + str(couldhave) + " people who use 'could of'---")
                print (done2)

            elif ('would of ' in str(comment).lower()) and (comment.id not in done3):

                done3.add(comment.id)
                comment.reply('Homophone error detected. [What is it?](http://www.reddit.com/r/SpellingB/comments/22bwnw/homophone_error) \
                              \n **would have** \n *Example:* I would have gotten away with it too... meddling kids. \
                              \n *** \n ^(Parent comment may have been edited/deleted.)')
                wouldhave += 1

                with open("wouldhave_comment_id.txt", "a") as outfile:
                outfile.write(comment.id + " ")

                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " ---FOUND A TOTAL OF " + str(wouldhave) + " people who use 'would of'---")
                print (done3)

            elif ('must of ' in str(comment).lower()) and (comment.id not in done4):

                done4.add(comment.id)
                comment.reply('Homophone error detected. [What is it?](http://www.reddit.com/r/SpellingB/comments/22bwnw/homophone_error) \
                              \n **must have** \n *Example:* It must have been love but it\'s over now. \
                              \n *** \n ^(Parent comment may have been edited/deleted.)')
                musthave += 1
                
                with open("musthave_comment_id.txt", "a") as outfile:
                outfile.write(comment.id + " ")
                
                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " ---FOUND A TOTAL OF " + str(musthave) + " people who use 'must of'---")
                print (done4)

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
                        

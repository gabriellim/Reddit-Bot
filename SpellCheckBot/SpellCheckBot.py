'''
SpellCheckBot by /u/ddNTP

[Python 3] SpellCheckBot is designed to search for comments on Reddit that have spelling mistakes...

--------------------
       Stats:
--------------------

Highest rated comment /r/leagueoflegends -  http://www.reddit.com/r/leagueoflegends/comments/21bgng/i_killed_my_teammate/cgbqu89?context=3

As of March 28 2014, SpellCheckBot has detected:
* 7 instances of should of
* 4 instances of could of
* 2 instances of would of
* 0 instances of effected me   (That incident really affected my friend)

--------------------
       Bugs:
--------------------

1. would offer is detected as would of*** which triggers the would of -> would have. Same thing happens to could offer
   and should offer.

   PROPOSED FIX:
   have the search term as 'would of ' instead of 'would of'
'''

# D.O.B.
DOB = "March 24 2014"

# Version
version = "1.0.1"

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

def affectedme_comment_id():
    with open("affectedme_comment_id.txt", "wt") as out_file:
        for i in done4:
            out_file.write(i + " ")

## START HERE ----------------------------------------------------------------------------------------------------------------

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

running = True
while running:
    try:
        # COUNTER
        count = 0 
        
        # SCAN COMMENTS
        comments = bot.get_comments('all', limit = 700)
        for comment in comments:
            count += 1
                        
            if ('should of ' in str(comment).lower()) and (comment.id not in done1):

                # REPLY TO COMMENT
                done1.add(comment.id)
                comment.reply('>*should have* : as in I should have taken the bullet for you. \n >> ^(Help me help you improve in English!)')
                shouldhave += 1
                shouldhave_comment_id()

                # CONSOLE DEBUG
                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " ---FOUND A TOTAL OF " + str(shouldhave) + " people who use 'should of'---")
                print (done1)

            elif ('could of ' in str(comment).lower()) and (comment.id not in done2):
                
                done2.add(comment.id)
                comment.reply('>*could have* : as in I could have eaten that last slice of pizza. \n >> ^(Help me help you improve in English!)')
                couldhave += 1
                couldhave_comment_id()

                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " ---FOUND A TOTAL OF " + str(couldhave) + " people who use 'could of'---")
                print (done2)

            elif ('would of ' in str(comment).lower()) and (comment.id not in done3):

                done3.add(comment.id)
                comment.reply('>*would have* : as in I would have gotten away with it too... meddling kids. \n >> ^(Help me help you improve in English!)')
                wouldhave += 1
                wouldhave_comment_id()

                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " ---FOUND A TOTAL OF " + str(wouldhave) + " people who use 'would of'---")
                print (done3)

            elif ('effected me' in str(comment).lower()) and (comment.id not in done4):

                done4.add(coment.id)
                comment.reply('>*affected me* : as in that incident really affected me. \n >> ^(Help me help you improve in English!)')
                affectedme += 1
                affectedme_comment_id()

                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print (timeset + " ---FOUND A TOTAL OF " + str(affectedme) + " people who use 'effected me'---")
                print (done4)

            else:
                pass

        timeset = time.strftime("%d/%m/%y %H:%M:%S")
        print (timeset + " Just scanned " + str(count) + " comments.")
        sleep(30)
		
    # ERROR # Exception as e
    except praw.errors.RateLimitExceeded:
        timeset = time.strftime("%d/%m/%y %H:%M:%S")
        print (timeset + " --ERROR-- Rate limit exceeded.")
        sleep(150) # IF ERROR OCCURED, SLEEP FOR 150 SECONDS
                        

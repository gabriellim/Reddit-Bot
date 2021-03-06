'''
SpellCheckBot by /u/ddNTP

[Python 3] SpellCheckBot is designed to search for comments on Reddit that have spelling mistakes...


-----------------------------------------------------------------------------------------------------------------------------------------------
    Banned from:                                    Reason:                                 Link:
-----------------------------------------------------------------------------------------------------------------------------------------------

/r/nfl              28 March 2014 @ ~6:40  PM       We don't allow novelty accounts         http://www.reddit.com/message/messages/1pl3bu
/r/funny            28 March 2014 @ ~7:01  PM       Bots are not allowed                    http://www.reddit.com/message/messages/1p8gq9
/r/leagueoflegends  28 March 2014 @ ~7:16  PM       We don't allow novelty bots             http://www.reddit.com/message/messages/1p8gww
/r/xboxone          31 March 2014 @ ~7:01  AM       We don't want junk bots                 http://www.reddit.com/message/messages/1pitsw
/r/asoiaf            3 April 2014 @ ~12:31 PM       Bots are not allowed                    http://www.reddit.com/message/messages/1pwd26
/r/relationships     6 April 2014 @ ~2:25  PM       Pending reply                           http://www.reddit.com/message/messages/1q8wyp
/r/seireitei         6 April 2014 @ ~4:24  PM       Bots are not allowed                    http://www.reddit.com/message/messages/1q9di0
/r/morbidreality     7 April 2014 @ ~12:09 AM       Novelty bots are not allowed            http://www.reddit.com/message/messages/1qb2bo
/r/mindcrack         7 April 2014 @ ~1:49  AM       No value added to the discussion        http://www.reddit.com/message/messages/1qb8gd
/r/politics          8 April 2014 @ ~12:23 PM       Bots are not allowed                    http://www.reddit.com/message/messages/1qhbgc                           
/r/cringepics        8 April 2014 @ ~8:12  AM       Bots are not allowed                    http://www.reddit.com/message/messages/1qghc7
/r/drugs             9 April 2014 @ ~7:11  AM       Useless bot are banned                  http://www.reddit.com/message/messages/1qksj9
/r/gaming            9 April 2014 @ ~4:52  PM       Bots are not allowed                    http://www.reddit.com/message/messages/1qmxj4
/r/soccer            9 April 2014 @ ~5:27  PM       Bots are not allowed                    http://www.reddit.com/message/messages/1qn2b0
/r/nba               9 April 2014 @ ~6:16  PM       Irrelevant bots are not allowed         http://www.reddit.com/message/messages/1qn6bm

--------------------
       Stats:
--------------------

Since March 24 2014 8:30 PM PST
As of April 9 2014 9:32 PM PST
      
SpellCheckBot has sent out:
* 271 instances of should have          (search for should of)
* 182 instances of could have           (search for could of
* 319 instances of would have           (search for would of)
* 47   instances of must have           (search for must of)

------------------------
       Milestones:
------------------------

1000 comment karma   April 2 2014 ~11:28 PM PST
2000 comment karma   April 7 2014 ~4:15  AM PST
3000 comment karam   ? ? ? ? ? ? ? ? ? ? ? ? ? 

'''

# D.O.B.
DOB = "March 24 2014"

# Version
version = "1.1.8"

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
done5 = set()

## START HERE -------------------------------------------------------------------------------------------------------------------

t = 15    ## Initial sleep before bot runs
    
shouldhave = 0
couldhave = 0
wouldhave = 0
musthave = 0
faiap = 0

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
                        
            if ('should of ' in str(comment).lower()) and (comment.id not in done1) and ('should of course' not in str(comment).lower()):

                # REPLY TO COMMENT
                done1.add(comment.id)
                comment.reply('Grammar error detected. [What is it?](http://www.reddit.com/r/SpellingB/comments/22bwnw/homophone_error) \
                              \n **should have** \n *Example:* I should have never thought horseback riding would be any better than ziplining. \
                              \n *** \n ^(Parent comment may have been edited/deleted.) ^[STATS](http://www.reddit.com/r/SpellingB/comments/22o42h/stats/)')
                shouldhave += 1

                # RECORD comment.id
                with open("shouldhave_comment_id.txt", "a") as outfile:
                    outfile.write(comment.id + " ")

                # CONSOLE DEBUG
                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print(timeset + " ---FOUND A TOTAL OF " + str(shouldhave) + " people who use 'should of'---")
                print(done1)

            elif ('could of ' in str(comment).lower()) and (comment.id not in done2) and ('could of course' not in str(comment).lower()):
                
                done2.add(comment.id)
                comment.reply('Grammar error detected. [What is it?](http://www.reddit.com/r/SpellingB/comments/22bwnw/homophone_error) \
                              \n **could have** \n *Example:* I could have taken the earlier train. \
                              \n *** \n ^(Parent comment may have been edited/deleted.) ^[STATS](http://www.reddit.com/r/SpellingB/comments/22o42h/stats/)')
                couldhave += 1

                with open("couldhave_comment_id.txt", "a") as outfile:
                    outfile.write(comment.id + " ")
        
                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print(timeset + " ---FOUND A TOTAL OF " + str(couldhave) + " people who use 'could of'---")
                print(done2)

            elif ('would of ' in str(comment).lower()) and (comment.id not in done3) and ('would of course' not in str(comment).lower()):

                done3.add(comment.id)
                comment.reply('Grammar error detected. [What is it?](http://www.reddit.com/r/SpellingB/comments/22bwnw/homophone_error) \
                              \n **would have** \n *Example:* I would have gotten away with it too... meddling kids. \
                              \n *** \n ^(Parent comment may have been edited/deleted.) ^[STATS](http://www.reddit.com/r/SpellingB/comments/22o42h/stats/)')
                wouldhave += 1

                with open("wouldhave_comment_id.txt", "a") as outfile:
                    outfile.write(comment.id + " ")

                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print(timeset + " ---FOUND A TOTAL OF " + str(wouldhave) + " people who use 'would of'---")
                print(done3)

            elif ('must of ' in str(comment).lower()) and (comment.id not in done4):

                done4.add(comment.id)
                comment.reply('Grammar error detected. [What is it?](http://www.reddit.com/r/SpellingB/comments/22bwnw/homophone_error) \
                              \n **must have** \n *Example:* It must have been love but it\'s over now. \
                              \n *** \n ^(Parent comment may have been edited/deleted.) ^[STATS](http://www.reddit.com/r/SpellingB/comments/22o42h/stats/)')
                musthave += 1
                
                with open("musthave_comment_id.txt", "a") as outfile:
                    outfile.write(comment.id + " ")
                
                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print(timeset + " ---FOUND A TOTAL OF " + str(musthave) + " people who use 'must of'---")
                print(done4)

            elif ('for all intensive purposes ' in str(comment).lower()) and (comment.id not in done5):

                done5.add(comment.id)
                comment.reply('Grammar error detected. [What is it?](http://www.reddit.com/r/SpellingB/comments/22bwnw/homophone_error) \
                              \n **for all intents and purposes** \
                              \n *** \n ^(Parent comment may have been edited/deleted.) ^[STATS](http://www.reddit.com/r/SpellingB/comments/22o42h/stats/)')
                faiap += 1

                with open("forallintents_comment_id.txt", "a") as outfile:
                    outfile.write(comment.id + " ")

                timeset = time.strftime("%d/%m/%y %H:%M:%S")
                print(timeset + " ---FOUND A TOTAL OF " + str(faiap) + " people who use 'for all intentsive purposes'---")
                print(done5)

            else:
                pass

        timeset = time.strftime("%d/%m/%y %H:%M:%S")
        print(timeset + " Just scanned " + str(count) + " comments.")
        sleep(20)
		
    # ERROR # Exception as e: # praw.errors.RateLimitExceeded:
    except Exception as e:
        timeset = time.strftime("%d/%m/%y %H:%M:%S")
        print(timeset + " --ERROR-- Rate limit exceeded.")
        sleep(300) # IF ERROR OCCURED, SLEEP FOR 300 SECONDS

## FIN --------------------------------------------------------------------------------------------------------------------------                       

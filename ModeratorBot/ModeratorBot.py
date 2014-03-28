'''

ModeratorBot by /u/ddNTP

[Python 3] A Reddit bot designed to first search for threads with a [Serious] tag. ModeratorBot will then
           post a comment advising users that comments which do not contribute to the discussions will be
           reported and probably removed by the subreddit moderators.

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
from collections import dequeu

# Set subreddit to be moderated 
subreddit = ""    ### COMPLETE THIS

# User Agent
bot = praw.Reddit("ModeratorBot " + str(version) + " by /u/ddNTP")

# Track thread_id so that ModeratorBot only makes one post per thread
done = dequeue(maxlen = 200)

# Record thread_id in a .txt file
def record_thread_id():
	with open("record_thread_id.txt", "wt") as out_file:
		for i in done:
			out_file.write(i + " ")


## START HERE -------------------------------------------------------------------------------------------------------

def login():
	username = input("Reddit username: ")    ### COMPLETE THIS
	password = input("Reddit password: ")    ### COMPLETE THIS
	bot.login(username, password)
	return username


loggedin = False
while not loggedin:
	try:
		timeset = time.strftime("%d/%m/%y %H:%M:%S")
		print(timeset + " Logging into Reddit...")
		username = login()
		loggedin = True
		print(timeset + " Login successful!")
	except praw.errors.InvalidUserPass:
		print("Invalid username/password, please reauthenticate.")

def main():
	sub = bot.get_subreddit(subreddit).get_new()
	for i in sub:
		# Check if thread has [serious] tag and if bot hasn't already posted in the thread
		if "[serious]" in i.title.lower() and i.id not in done: 
		        print (i.title)
			i.add_comment("**Attention!** Please remember that the OP of this thread has marked this post with a **[Serious]** tag. \n" "Any replies that are jokes, puns, off-topic, non-contributory or deisnged to derail the thread will be reported and removed by the moderators. \n" "*Please report anyone who violates this. Thanks for reading and as usual, get back to Reddit, citizen.*")
			sleep(3)
		        done.append(i.id)
		        record_thread_id()

running = True
while True:
	try:
		main()
		sleep(10)
	except praw.errors.RateLimitExceeded:
		sleeptime = 45
		timeset = time.strftime("%d/%m/%y %H:%M:%S")
		print(timeset + " Rate limit exceeded - sleep for " + str(sleeptime))
		sleep(sleeptime) # PRAW rate limit exceeded, bot will sleep for sleeptime seconds

## END

 RedditBot
===========

A collection of bots written in Python 3 designed to interact with PRAW: The Python Reddit API Wrapper.

[**ModeratorBot**](https://github.com/gabriellim/RedditBot/blob/master/ModeratorBot/ModeratorBot.py)

Within a subreddit, ModeratorBot will first search for threads with the [Serious] tag, which indicates that the OP (original poster) has designated his thread to only be commented by serious posters i.e. no puns, no jokes, no spam, no comments that will derail the discussion. Usually ModeratorBot will be the first to post a comment to the serious thread with a message that advises users about the consequences of not adhering to the [Serious] tag. Their comments will be recorded and subsequently removed by the subreddit moderators.

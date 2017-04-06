 RedditBot
===========

A collection of bots written in python 3 based on the Python Reddit API Wrapper(PRAW).

[**ModeratorBot**](https://github.com/gabriellim/RedditBot/blob/master/ModeratorBot/ModeratorBot.py)

A subreddit is a sub-topic in Reddit.com, similar to a topic within a traditional forum. Within a subreddit, ModeratorBot will first search for threads with the [Serious] tag, which indicates that the OP (original poster) has designated his thread to only accepting comments that are serious posters, which means no puns, no jokes, no spam, no comments that will derail the discussion. Usually ModeratorBot will be the first to post a comment to the serious thread with a message that advises users about the consequences of not adhering to the [Serious] tag. Their comments will be recorded and subsequently removed by the subreddit moderators.


[**SpellCheckBot**](https://github.com/gabriellim/RedditBot/blob/master/SpellCheckBot/SpellCheckBot.py)

SpellCheckBot searches for homophone errors (usage of words that have the same pronunciation but differ in meaning or spelling).

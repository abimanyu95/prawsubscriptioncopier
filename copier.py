#add credentials in creds_to.py and creds_from.py in the same directory as this file and run the application to copy subscriptions from one account to another
import praw
import creds_from, creds_to #creds_from : credentials of account from which the subs have to copied; creds to : credentials of the account to which the subs have to be copied

reddit_from = praw.Reddit(client_id = creds_from.client_id,
                          client_secret=creds_from.client_secret,
                          user_agent=creds_from.user_agent,
                          username=creds_from.username,
                          password=creds_from.password)

reddit_to = praw.Reddit(client_id = creds_to.client_id,
                        client_secret=creds_to.client_secret,
                        user_agent=creds_to.user_agent,
                        username=creds_to.username,
                        password=creds_to.password)


x= int(0)
for sub in reddit_from.user.subreddits(limit=None):
        subreddit = reddit_to.subreddit(str(sub))  #str(sub) gets just the name of the sub as a string insted of a subreddit instance
        subreddit.subscribe()
        x=x+1                                      #just a counter to check how many subscriptions

print(x)



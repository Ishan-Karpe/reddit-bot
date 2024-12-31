import praw
#praw is a python wrapper for the Reddit API
print('\033[1m' + 'top' + '\033[0m')
username="InformalAdeptness204"
password="Cha9rewoodbridge"
client_id="L-BcoXw9l662wqs5kHYc6g"
client_secret = "pSWegJ-kJZQBYSuc60BHZ3tZKGKp6w"

# remeber to replace the above values with your own values from reddit bot website

reddit = praw.Reddit( #creating a reddit instance with the above credentials, user_agent is a string that describes the bot
    client_id=client_id,
    client_secret=client_secret,
    user_agent="test_bot",
    username=username,
    password=password
)

print(reddit.user.me()) #prints the username of the bot

subreddit = reddit.subreddit("learnpython") #specifying the subreddit to monitor
print(subreddit)
hot_25_submissions = subreddit.hot(limit=25) #the top 25 hot submissions in the subreddit of learnpython
for submission in hot_25_submissions:
    print("Title: ", submission.title) # prints the title of the submission
    print("Text: ", submission.selftext) # prints the text of the submission
    print("Score: ", submission.score) # prints the score of the submission

# the code above will read what is on the front page of the subreddit learnpython
# now let's do the same for the other cateogies of the subreddit


print('\033[1m' + 'new' + '\033[0m') #special print statement to make the text bold
new_25_submissions = subreddit.new(limit=25, time_filter='day') #the top 25 new submissions in the subreddit of learnpython
for submission in new_25_submissions:
    print("Title: ", submission.title) # prints the title of the submission
    print("Text: ", submission.selftext) # prints the text of the submission
    print("Score: ", submission.score) # prints the score of the submission

print('\033[1m' + 'top' + '\033[0m')
top_25_submissions = subreddit.top(limit=25, time_filter='all') #the top 25 top submissions in the subreddit of learnpython
for submission in top_25_submissions:
    print("Title: ", submission.title) # prints the title of the submission
    print("Text: ", submission.selftext) # prints the text of the submission
    print("Score: ", submission.score) # prints the score of the submission


print('\033[1m' + 'rising' + '\033[0m')
rising_25_submissions = subreddit.rising(limit=25) #the top 25 rising submissions in the subreddit of learnpython
for submission in rising_25_submissions:
    print("Title: ", submission.title) # prints the title of the submission
    print("Text: ", submission.selftext) # prints the text of the submission
    print("Score: ", submission.score) # prints the score of the submission

print('\033[1m' + 'END' + '\033[0m')



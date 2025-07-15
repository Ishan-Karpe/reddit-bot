# Happy New Year! 2025

import praw
import os
from openai import OpenAI
from dotenv import load_dotenv
#praw is a Python wrapper for the Reddit API
username = "" # your Reddit username
password = "" # password you use to login to reddit
client_id = "" # under personal token
client_secret = "" # next to the word secret


load_dotenv()
api_key = os.getenv('OPENAI_API_KEY') # fill in your key in .env

''' Remember to replace the above values with your values'''

reddit = praw.Reddit( #creating a reddit instance with the above credentials, user_agent is a string that describes the bot
    client_id=client_id,
    client_secret=client_secret,
    user_agent="test_bot",
    username=username,
    password=password
)

print(reddit.user.me()) #prints the username of the bot

subreddit = reddit.subreddit("learnpython") #specifying the subreddit to monitor, use your own subreddit of your choice
print(subreddit)
hot_25_submissions = subreddit.hot(limit=25) 
for submission in hot_25_submissions:
    print("Title: ", submission.title)
    print("Text: ", submission.selftext) 
    print("Score: ", submission.score) 


print('\033[1m' + 'new' + '\033[0m') #special print statement to make the text bold
new_25_submissions = subreddit.new(limit=25) #the top 25 new submissions in the subreddit of learnpython
for submission in new_25_submissions:
    print("Title: ", submission.title) 
    print("Text: ", submission.selftext) 
    print("Score: ", submission.score)

print('\033[1m' + 'top' + '\033[0m')
top_25_submissions = subreddit.top(limit=25, time_filter='all') #the top 25 top submissions in the subreddit of learnpython
for submission in top_25_submissions:
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)


print('\033[1m' + 'rising' + '\033[0m')
rising_25_submissions = subreddit.rising(limit=25) #the top 25 rising submissions in the subreddit of learnpython
for submission in rising_25_submissions:
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)

print('\033[1m' + 'END' + '\033[0m')


# Now we submit our post to the subreddit
subreddit = reddit.subreddit("testingground4bots") #specifying the subreddit to monitor, no ban on this subreddit
print(subreddit)
subreddit.submit("This is a test post", selftext="This is a test post by a bot, How are you?") 
subreddit.submit("This is a test post 2", selftext="Happy New Year! 2025")

# submit(title, description) is a function that submits a post to the subreddit

# now we will comment on a post, or also fetch comments

submission = reddit.submission("1hq2eye")
comments = submission.comments 
print(submission.title) 
print(submission.comments) 
print(len(submission.comments))
comments.replace_more(limit=None)
print(len(submission.comments)) 

# ai response to comments using chatgpt and your API KEY

for comment in comments:
    if 'GitHub' in comment.body:
        ai_input = comment.body
        response = OpenAI().chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": ai_input}
            ],
            max_tokens=100
        )
        comment.reply(response.choices[0].message.content)  


for comment in comments:
    if 'GitHub' in comment.body:
        comment.reply("I am a bot, and this action was performed automatically. Please contact the moderators of this subreddit if you have any questions or concerns.") # standard without AI



'''
In summary, this program does the following:
1. Log in to Reddit using the credentials provided
2. Print the top 25 hot submissions in the subreddit learnpython, as well as similar information for the top, new, and rising submissions
3. Submit two posts to the subreddit testingground4bots
4. Comments on a post in the subreddit learnpython
5. Uses the OpenAI API to respond to comments that contain the word "GitHub"

Check my README for any additional information  
'''




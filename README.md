# Reddit Bot with AI-generated comments and replies [customizable]

### This Reddit bot uses Praw (Python Reddit API Wrapper) to connect to Reddit's API  and fetch data from reddit and uses OPENAI API to process or analyze that data to reply to comments/posts. 
to make this program work you need:
- openai API KEY from OpenAI API (need to pay)
    - create .env and store OPENAI_API_KEY='key' key is your key
- https://www.reddit.com/prefs/apps Go to this site and create a new bot, set it as a script, give it a name, and redirect URI is https://localhost:8080
    - under personal use script is your client ID, copy and paste into client_id
    - username is Reddit user, password is your password
    - client long token is where the client_secret value IS next to the word secret
- you can also customize which subreddit to monitor and which specific submission ID you want, this example uses r/learnpython
- install required packages as well
  - pip install -r requirements.txt

- if you get any pip errors create a virtual env and rerun

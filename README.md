# Reddit Bot with AI-generated comments and replies [customizable]

### This Reddit bot uses Praw to connect to Reddit's API and uses OPENAI to reply to comments using the comment body. It also scrapes data for the front page of the subreddit

in order to make this program work you need:
- openai API KEY
    - create .env and store OPENAI_API_KEY='key' key is your key
- https://www.reddit.com/prefs/apps go to this site and create a new bot, set as script, give it a name, and redirect uri is https://localhost:8080
    - under personal use script is your client id , copy paste into client_id
    - username is reddit user, password is your password
    - client long token is where the client_secret value is.
- you can also customize which subreddit to montior and which specific submission ID you want
- install required packages as well

- if you get any pip errors create a virtual env and rerun

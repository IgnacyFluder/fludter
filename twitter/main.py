import tweepy
import random

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAAjbpgEAAAAAuhrmyT3Oi6nxWhqsl0hWdSoXCqA%3DyiNyZyDsoptLvTY1xlKDY3EE7jYZ4H9krr66JreR7AeJ7vfUJi'
consumer_key = 'fI9K6GqQUwPo8FtFFJyRXBUwE'
consumer_secret = 'WKx0PM9sEQOBiXduuzSvLA70IfGthP3QVbbUFjOnBKoZlXjiND'
access_token = '1594793771178364928-CjQ1KDSv4o0hf8t1SuX6cU03FgSCfY'
access_token_secret = 'MAYa44A5OSczbKZRNvmbFhU2ii7G1kUhuIW7O580fPaZu'

# for v1.1
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

api = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)


#adds a random number scince twitter does not allow duplicate tweets
tweet = "Hello, Twitter!"+str(random.randint(1,1000))
api.create_tweet(text=tweet)
print("Tweet posted successfully!")


tweet_id = '1697498734517428337'
screen_name = 'IgnacyFluder'

reply_text = "Thanks for your tweet!"+str(random.randint(1,1000))
api.create_tweet(text=reply_text, quote_tweet_id=tweet_id)
print("Reply posted successfully!")

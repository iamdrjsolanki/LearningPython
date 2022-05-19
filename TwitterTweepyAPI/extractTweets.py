import tweepy
import webbrowser
import time

consumerKey = 'GMf3zN2u5DCWbvcxrbi7oA7qv'
consumerSecret = 'ONuuPcoHOG7wMmP6HWaWLI4ddyMJvMpnxpN4bauJn0HQKw0jY1'
callbackUri = 'oob'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret, callbackUri)
redirectUrl = auth.get_authorization_url()
print(redirectUrl)

webbrowser.open(redirectUrl)

userPinInput = input("Whats the pin value?")
auth.get_access_token(userPinInput)
print(auth.access_token, auth.access_token_secret)

api = tweepy.API(auth)
#newTweet = api.update_status("Heelp world this is my first tweet!!")
tweetsByUsername = tweepy.Cursor(api.search_tweets, q="@elonmusk", tweet_mode='extended').items(5)

for tweet in tweetsByUsername:
    text = tweet._json["full_text"]
    print(text)
    print(tweet.favorite_count)
    print(tweet.retweet_count)
    print(tweet.created_at)



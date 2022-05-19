import tweepy
import webbrowser
import time

consumerKey = 'GMf3zN2u5DCWbvcxrbi7oA7qv'
consumerSecret = 'ONuuPcoHOG7wMmP6HWaWLI4ddyMJvMpnxpN4bauJn0HQKw0jY1'
callbackUri = 'oob'

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAMAqbAEAAAAAz9qtI21yJyDxiDabqUokEcXo1MU%3DPwkkpNkzOvG5HgQSkwU1UYNKaYZFHmmkXhx9OhYHi5vtVCuvMu')

query = 'from:CNBCTV18Live'

tweets = client.search_recent_tweets(query=query, tweet_fields=['referenced_tweets', 'created_at'], max_results=11)

for tweet in tweets.data:
    print("Tweet: "+tweet.text)
    print("created_at")
    print(tweet.created_at)
    
    if (tweet.referenced_tweets[0] != None):
        print(tweet.referenced_tweets[0])
    #if (tweet.referenced_tweets[0] != None and tweet.referenced_tweets[0] == "retweeted"):
    #    retweet = client.get_tweets(ids=tweet.referenced_tweets.id, tweet_fields=['created_at'])
    #    print("Retweeted Tweet: "+retweet.text)
    #if len(tweet.context_annotations) > 0:
        #print(tweet.context_annotations)



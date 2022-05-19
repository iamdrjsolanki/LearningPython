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

#print(auth.access_token, auth.access_token_secret)

api = tweepy.API(auth)

me = api.me()

print(me.screen_name)




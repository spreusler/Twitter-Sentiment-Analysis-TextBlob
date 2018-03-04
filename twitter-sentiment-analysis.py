# Import Bibliotheken
import tweepy
# from textblob import TextBlob

# Deutsche Datenbank
from textblob_de import TextBlobDE as TextBlob

# Authentifizierung
consumer_key= 'consumer_key'
consumer_secret= 'consumer_secret'

# Registrierung als Twitter App wird benötigt
access_token='access_token'
access_token_secret='access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Suche nach Tweets über den Hamburger Sportverein
public_tweets = api.search('HSV')

# Ausgabe der Tweets
for tweet in public_tweets:
    print(tweet.text)
    
    # Bewertung der Tweets
	# Polarity: Wertebereich -1 bis 1: Negative oder positive Aussage?
	# Subjectivity: Wertebereich -1 bis 1: Subjektive oder weniger subjektive Aussage?
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
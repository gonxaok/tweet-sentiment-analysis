import tweepy
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


consumer_key = 'CONSUMER KEY'
consumer_secret = 'CONSUMER SECRET'
access_token = 'ACCESS TOKEN'
access_token_secret = 'ACCESS TOKEN SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)


nombre_cuenta = 'CUENTA DE TWITTER'


tweets = api.user_timeline(screen_name=nombre_cuenta, count=10)


sia = SentimentIntensityAnalyzer()

positivos = 0
negativos = 0
for tweet in tweets:
    sentimiento = sia.polarity_scores(tweet.text)
    if sentimiento['compound'] > 0:
        positivos += 1
    elif sentimiento['compound'] < 0:
        negativos += 1

labels = ['Positivos', 'Negativos']
sizes = [positivos, negativos]
colors = ['green', 'red']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Análisis de sentimientos de los últimos 10 tweets de ' + nombre_cuenta)
plt.savefig('analisis_sentimientos.pdf')

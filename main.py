#Bu kısımda gerekli kütüphaneleri içe aktarıyoruz.
import tweepy

#Bu kısımda Twitter API'sine bağlanmak için gerekli bilgileri giriyoruz.
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

#Bu kısımda tweepy kütüphanesini kullanarak Twitter API'sine bağlanıyoruz.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Bu kısımda bir sözlük oluşturuyoruz. Bu sözlükte tweet konularının kaç kez geçtiği tutulacak.
tweet_konulari = {}

#Bu kısımda bir döngü oluşturuyoruz. Bu döngü süresince tweetler okunacak.
for tweet in tweepy.Cursor(api.search, q="#python", lang="en", since="2018-04-03").items():
    #Bu kısımda okunan tweetlerden tweet konuları alınıyor.
    tweet_konusu = tweet.text.split(" ")[0]

    #Bu kısımda tweet konularının kaç kez geçtiğini sözlükte tutuyoruz.
    if tweet_konusu in tweet

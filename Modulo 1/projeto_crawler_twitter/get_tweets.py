import json
from tweepy import OAuthHandler,Stream,StreamListener
from datetime import datetime

# key access .

consumer_key  = "zqvLm5PiN0M1Aafxl0S8lI72x"
consumer_secret = "FvY7FwoUzJHakb9byGFGCN97nO4Dv8WR6NyccKo4pUdnvyPA3o"
access_token = "1333545883485548544-LSzXZ1m6iUWwUKRDUnp4BOQ5qLhSG7"
access_secret = "AbBL5pOw9gu64eIZX4o0KBsGrSe2eBtNvYNIAsdjklbwi"


#define tweets
today = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
out = open(f"collected_tweets_{today}.txt","w")


# conection twitter

class MyListener(StreamListener):
  def on_data(self,data):
    
      itemString = json.dumps(data)
      out.write(itemString + "\n")
      return True

  def on_error(self,status):
      print(status)    

if __name__ == "__main__":
    my = MyListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    
    stream = Stream(auth,my)
    stream.filter(track=["Trump"])

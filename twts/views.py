from django.shortcuts import render
#from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


from django.http import HttpResponse



consumer_key="bNZhvARBiwVDwCXYiMM8UuSil"
consumer_secret="cWkNM4VMPkLwReTmXtlI4ZfvTKlR8NF1kKNt155OCYU2Hl2BbP"


access_token="4881087855-erCf1EUIN2sbAr79u8qhaMKQC4tPAdWCApYJ9f3"
access_token_secret="MfJuWK6dzdamtxca6zMmOKoAglwpheT9hZs4JDX5ZLKbh"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self,status):
        '''data.filter('",text"')
        saveFile=open('twit.csv','a')
        saveFile.write(data)
        saveFile.write('\n')
        saveFile.close()'''

        return (status)

    def on_error(self, status):
        print(status)



if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['GST'])
def twts(status):

    data=status.text()





    return HttpResponse(data)

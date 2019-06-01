from flask import Flask,render_template,request
import tweepy
from textblob import TextBlob

app=Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/',methods=['POST'])
def getvalue():
    name = request.form['name']
    consumer_key='q1JGNremrrRZRGQmYKGMItPD0'
    consumer_secret='N8JmQTcvyE8atBFIBGFD0ktBRFxWjfxx22rFbAOmuWpFLKlCGz'
    access_token='892363341112279040-J0UAAUGOHaSpSqlOcz7oV3b0POidAVr'
    access_token_secret='7r19lfBFQDgC5OACKEaiZr2XGo5JTpHr9Lp54sOAlIwnV'
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret);
    auth.set_access_token(access_token,access_token_secret);
    api=tweepy.API(auth)
    #public_tweets=api.search('Pavan kalyan')
    query=name
    max_tweets=20
    l=[]
    a=[]
    ne=[]
    public_tweets=[status for status in tweepy.Cursor(api.search,q=query).items(max_tweets)]
    for tweet in public_tweets:
        v=tweet.text
        v=v.split()
        w=""
        for i in v:
            try:
                i.encode('utf-8')
                w=w+i
            except:
                w+=""
        analysis= TextBlob(tweet.text)
        k=analysis.sentiment
        if(k[0]<0):
            a.append(w)
        elif(k[0]==0):
            ne.append(w)
        else:
            l.append(w)
    return render_template('pass.html', li1=l,li2=a,li3=ne,P=len(l),N=len(a),NE=len(ne))

if __name__ == '__main__':
    app.run(debug=True)
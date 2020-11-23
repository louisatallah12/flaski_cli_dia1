from flask import Flask
from redis import Redis, RedisError

import socket

# create a redis instance, from connection to redis-server
redis = Redis(host = "redis-server", db = 0)

app = Flask(__name__)

@app.route('/')

def hello() :
    return "<h1> Hello World ! </h1>" 
 @app.route('/visit')
 def incr_counter():
    try : 
        visits = redis.incr("counter")
    except : 
        visits = "<i> I could not connect to the redis server </i>"
    html = "<h1> Number of visits : {}</h1>".format(visits)

    return html

if __name__ == "__name__":
    app.run(debug = True, port = 80, host="0.0.0.0")
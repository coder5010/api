from instagram_private_api import Client, ClientCompatPatch
from flask import request
import json
from flask import jsonify

from flask import Flask
app = Flask(__name__) # Create an Instance

user_name = 'instagram alt username'
password = 'instagram alt password'

api = Client(user_name, password)


@app.route('/instagram') 
def main(): 
    username = request.args.get('username') 
    hehe = api.username_info(username)
    data = json.dumps(hehe)
    aa = json.loads(data)
    print(aa)
    return jsonify(
        username=username,
        full_name=aa['user']['full_name'],
        biography=aa['user']['biography'],
        posts=aa['user']['media_count'],
        followers=aa['user']['follower_count'],
        following=aa['user']['following_count'],
        private=aa['user']['is_private'],
        verified=aa['user']['is_verified']

    )

    #return aa['user']['biography']
app.run(host='0.0.0.0', port=5000, debug=True) 

from instagram_private_api import Client, ClientCompatPatch
import json
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

user_name = 'yourigname'
password = 'yourigpass'

api = Client(user_name, password)


@app.get('/instagram') 
async def read_item(username: str): 
    #username = str(Request.query_params)

    hehe = api.username_info(username)
    data = json.dumps(hehe)
    aa = json.loads(data)
    print(aa)
    this_dict = {
  "full_name": aa['user']['full_name'],
  "biography": aa['user']['biography'],
  "posts": aa['user']['media_count'],
  "followers": aa['user']['follower_count'],
  "following": aa['user']['following_count'],
  "private": aa['user']['is_private'],
  "verified": aa['user']['is_verified']
}
    return this_dict

    #return aa['user']['biography']
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

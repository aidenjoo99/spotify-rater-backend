import json
import os
import base64

from flask import Flask, request
from requests import post, get
from dotenv import load_dotenv
from db import db

app = Flask(__name__)
db_filename = PASS

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
  auth_string = client_id + ":" + client_secret
  auth_bytes = auth_string.encode("utf-8")
  auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

  url = "https://accounts.spotify.com/api/token"
  headers = {
    "Authorization": "Basic " + auth_base64,
    "Content-Type": "application/x-www-form-urlencoded"
  }
  data = { "grant_type": "client_credentials" }
  result = post(url, headers=headers, data=data)
  json_result = json.loads(result.content)
  token = json_result["access_token"]
  return token

def get_auth_token(token):
  return { "Authorization": "Bearer " + token }

token = get_token()

@app.route("/api/search/", methods=["GET"])
def search_song(token):
  url = "https://api.spotify.com/v1/search"
  headers = get_auth_token(token)
  q = request.args.get("query")
  if q: 
    query = f"?q={q}&type=album,artist,track&limit=10"
    query_url = query + url
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    return json_result
    
  return {}
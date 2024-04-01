from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    result = post(url, headers=headers, data=data)
    json_results = json.loads(result.content)

    token = json_results["access_token"]

    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}  # Add a space after 'Bearer'

def search_for_artist_name(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_results = json.loads(result.content)["artists"]["items"]

    if len(json_results) == 0:
        print("No artists named like this exists on Spotify ...")

    else:
        return json_results[0]



def main():
    token = get_token()
    print(search_for_artist_name(token, "Mattak")["name"])

if __name__ == "__main__":
    main()

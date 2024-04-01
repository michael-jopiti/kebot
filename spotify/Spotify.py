from dotenv import load_dotenv
import os, sys, base64, json
from requests import post, get

sys.path.append("/Users/michaeljopiti/kebot")

from spotify import sp_commands as commands

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


##################
# Start the Spotify API
##################

def main():
    token = get_token()
    print(commands.search_for_artist_name(token, "Mattak")["name"])

if __name__ == "__main__":
    main()

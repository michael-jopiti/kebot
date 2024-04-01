import os, sys, base64, json
from requests import post, get

sys.path.append("/Users/michaeljopiti/kebot/spotify")

from Spotify import get_token, get_auth_header


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
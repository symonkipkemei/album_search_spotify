import requests
import os


# parameters
authorization_token = os.environ["AUTH_TOKEN"]
spotify_artist_id = "0yOSvlhtID1BtqO5UUv5SL"
spotify_artist_album_endpoint = f"https://api.spotify.com/v1/artists/{spotify_artist_id}/albums"

# connect with spotify's restful api and obtain artist album of choice

def get_artist_album(auth_token:str,url:str)-> dict:
    """Get artist album

    Args:
        auth_token (str): Authorization token required
        url (str): spotify artist album end point

    Returns:
        dict: Returns a json encoded content (dictionary) with all information regarding the album
    """

    #query params to narrow down the request
    query_params = {
        "include_groups":"single,album,compilation,appears_on",
        "market":"US",
        "limit":50,
        "offset":5
    }

    #headers to include data type and authentication information
    headers = {
        "Accept":"application/json",
        "Authorization" : f"Bearer {auth_token}"
    }

    # http get request
    response = requests.get(url=url,params=query_params,headers=headers)

    # format response to json 
    response = response.json()


    return response


# abstract data from file
def main():
    response = get_artist_album(auth_token=authorization_token,url=spotify_artist_album_endpoint)

    # album list
    album_list = response["items"]

    # filter and enumerate the album type, name and release date

    for index, album in enumerate(album_list, 1):
        print("_____________________________________")
        print(f"Album number: {index}")
        print(f"Album type: {album['album_type']}")
        print(f"Album name: {album['name']}")
        print(f"Album name: {album['release_date']}")
        print("_____________________________________")

# dunder name 
if __name__ == "__main__":
    main()

    

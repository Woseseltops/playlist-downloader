def download_playlist(username,playlist_id,credential_file_location):

    from spotipy import Spotify,util
    from json import load

    #import the credentials
    credentials = load(open(credential_file_location))

    #Create an authenticated connection
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username,scope=scope,client_id=credentials['client_id'],
                                       client_secret=credentials['client_secret'],
                                       redirect_uri=credentials['redirect_url'])
    connection = Spotify(auth=token)

    #Mine the songs
    songs = []

    for track in  connection.user_playlist(username, playlist_id,fields="tracks,next")['tracks']['items']:
        songs.append((track['track']['artists'][0]['name'],track['track']['name']))

    #Gebruikersnaaam lostrekken, geheimen lostrekken

    return songs

def find_youtube_url(artist,song_title):

    import urllib.request
    import urllib.parse
    import re

    query_string = urllib.parse.urlencode({"search_query" : artist + ' - ' + song_title + ' album'})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})" class="yt-uix-sessionlink yt-uix-tile-link', html_content.read().decode())
    return search_results[0]

def save_youtube_video(url,output_location):

    from subprocess import check_output
    check_output('youtube-dl.exe --extract-audio --audio-format mp3 '+url+' -o "'+output_location+'"',shell=True)

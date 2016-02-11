import spotifyyoutubemp3
import json

SETTINGS_FILE_LOCATION = 'settings.json'

settings = json.load(open(SETTINGS_FILE_LOCATION))
playlist = spotifyyoutubemp3.download_playlist(settings['spotify_username'],settings['spotify_playlist_id'],
                                               'spotify_credential_file_location')

for artist, song_title in playlist:

    print('Getting link for '+artist+' - '+song_title)
    youtube_url = spotifyyoutubemp3.find_youtube_url(artist,song_title)

    print('Downloading '+artist+' - '+song_title)
    try:
        spotifyyoutubemp3.save_youtube_video(youtube_url,settings['output_folder']+artist+' - '+song_title+'.mp3')
    except:
        print('Error, continuing with next one')
        continue

#Future ideas
# Sync with playlist instead of download playlist
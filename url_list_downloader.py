import spotifyyoutubemp3
import json

SETTINGS_FILE_LOCATION = 'settings.json'
URL_LIST_FILE_LOCATION = 'to_download.tsv'

settings = json.load(open(SETTINGS_FILE_LOCATION))

for line in open(URL_LIST_FILE_LOCATION):

    songinfo, url = line.strip().split('\t')

    print('Downloading '+songinfo)
    try:
        spotifyyoutubemp3.save_youtube_video(url,settings['output_folder']+songinfo+'.mp3')
    except:
        print('Error, continuing with next one')
        continue

#Future ideas
# Sync with playlist instead of download playlist
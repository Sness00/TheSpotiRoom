from modules import spotipy_custom
from modules import credentials_window
import webbrowser
import os
import dotenv

#####################################################################################
#                            SPOTIPY                                                #
##################################################################################### 

class spotipy_connection():

    client_id = None
    client_secret = None
    redirect_uri = None
    scope = None
    token = None
    sp = None

    def __init__(self):
        if dotenv.find_dotenv(filename='./modules/credentials.env') == '':
            cred_wind = credentials_window.cred_window()
            self.client_id, self.client_secret, self.redirect_uri = cred_wind.display_window()
            if self.client_id != '' and self.client_secret != 'none' and self.redirect_uri != '':
                f = open('./modules/credentials.env', 'w')
                f.write('CLIENT_ID=' + self.client_id + '\n')
                f.write('CLIENT_SECRET=' + self.client_secret + '\n')
                f.write('REDIRECT_URI=' + self.redirect_uri)
                f.close()
                os.environ["CLIENT_ID"] = self.client_id
                os.environ["CLIENT_SECRET"] = self.client_secret
                os.environ["REDIRECT_URI"] = self.redirect_uri
        else:
            dotenv.load_dotenv('./modules/credentials.env')
            self.client_id = os.environ.get('CLIENT_ID')
            self.client_secret = os.environ.get('CLIENT_SECRET')
            self.redirect_uri = os.environ.get('REDIRECT_URI')

        # List of authorizations for spotify web api
        scope = 'playlist-modify-public, playlist-modify-private, app-remote-control, streaming, user-read-playback-state, '
        scope = scope + 'user-modify-playback-state, user-read-currently-playing, '
        self.scope = scope

        self.token = spotipy_custom.oauth2.SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret,
                                                        redirect_uri=self.redirect_uri, scope=self.scope, username='a')
        self.sp = spotipy_custom.Spotify(auth_manager=self.token)

    def run(self):
        devices = self.sp.devices()['devices']
        while len(devices) == 0:
            devices = self.sp.devices()['devices']

        dev_id = devices[0]['id']
        
        if self.sp.current_playback() == None or self.sp.current_playback()['is_playing'] == False:
            while True:
                try:
                    self.sp.volume(0, dev_id)
                    self.sp.start_playback(device_id=dev_id)
                    break
                except:
                    if self.sp.current_playback() != None or self.sp.current_playback()['is_playing'] == True:
                        break

        current_play = self.sp.current_playback()
        while(current_play == None or current_play['is_playing'] == False):
            current_play = self.sp.current_playback()
        
        playlist = self.sp.playlist_tracks(playlist_id='3xQDsuEHX7MKaLyS79Kqsn')
        while True:
            try:
                queue = self.sp.queue()['queue']
                break
            except:
                pass
        for song in playlist['items']:
            present = False
            for song_in_queue in queue:
                if song['track']['id'] == song_in_queue['id']:
                    present = True
            if not present:
                while True:
                    try:
                        self.sp.add_to_queue(song['track']['id'])
                        break
                    except:
                        pass
        while True:
            try:
                self.sp.next_track(dev_id)
                break
            except:
                pass
        while True:
            try:
                self.sp.volume(100, dev_id)
                break
            except:
                pass

    def spotipy_target(self, python_osc_object, quit_object):
        old = None
        danceability = 0
        tempo = 0
        tempo_period = 0
        
        while True:
            if quit_object.get_quit():
                break

            while True:
                try:
                    current = self.sp.current_playback()['item']
                    break
                except:
                    if self.sp.current_playback() is None:
                        quit_object.quit_function()
                        break
                    pass  
            if current != old:
                audio_features = self.sp.audio_features(current['id'])
                danceability = audio_features[0]['danceability']
                tempo = audio_features[0]['tempo'] + 0.00001
                tempo_period = 30/tempo
                if audio_features[0]['energy'] > 0.5 and audio_features[0]['valence'] > 0.5:
                    mood = 4
                elif audio_features[0]['energy'] > 0.5 and audio_features[0]['valence'] <= 0.5:
                    mood = 1
                elif audio_features[0]['energy'] <= 0.5 and audio_features[0]['valence'] <= 0.5:
                    mood = 2
                else:
                    mood = 3            
                python_osc_object.send_static(mood, "/mood")            
                title = current['name']
                if len(title) <= 6:
                    title_size = 0.6
                elif len(title) <= 10:
                    title_size = 0.40
                elif len(title) <= 35:
                    title_size = 0.35
                elif len(title) <= 70:
                    title_size = 0.33
                elif len(title) <= 110:
                    title_size = 0.30
                else:
                    title_size = 0.3
                python_osc_object.send_static(danceability, "/danceability")
                python_osc_object.send_static(tempo_period, "/period")
                python_osc_object.send_static(audio_features[0]['mode'], "/mode")
                python_osc_object.send_static(title, "/song")
                python_osc_object.send_static(title_size, '/title_size')
                old = current

    def stop_spotify(self):
        if self.sp.current_playback()['is_playing'] and self.sp.current_playback() is not None:
            self.sp.pause_playback()

    def open_spotify(self, quit_object):
            webbrowser.open('https://open.spotify.com/playlist/3xQDsuEHX7MKaLyS79Kqsn')
    
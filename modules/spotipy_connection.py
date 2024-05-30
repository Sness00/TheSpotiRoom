from modules import spotipy_custom
import webbrowser

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
        # self.client_id = 'f398f6f7935c42329df3527a5f08085d'
        # self.client_secret = 'a92b9fea0d9d495ea1b4f3d911ca62e8'
        # self.redirect_uri = 'https://www.google.com'
        self.client_id = '985802cfac79408da56061d424895817'
        self.client_secret = '119e677d57b641aa83a7d7338aafa6fc'
        self.redirect_uri = 'https://www.google.it/'
        # self.client_id = '1b3f903e755b4d1cbfb6b7c98491edce' #andre
        # self.client_secret = 'c769bb8c99d2444cb6f91dc0d314ef26' 
        # self.redirect_uri = 'https://www.google.com'
        # self.client_id = '421bf7f958744400b1748f1f6c0ee5dc'
        # self.client_secret = '1957fa73cb9f40609da215761cba259b'
        # self.redirect_uri = 'https://www.google.com'

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
    
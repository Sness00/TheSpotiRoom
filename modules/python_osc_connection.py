from pythonosc.udp_client import SimpleUDPClient

#####################################################################################
#                            PYTHON-OSC                                             #
#####################################################################################

class python_osc_connection():

    client = None

    def __init__(self):
        ip = "127.0.0.1"
        port = 4444
        self.client = SimpleUDPClient(ip, port) # Create client

    def send_features(self, features):
        self.client.send_message("/energy", features[0][0])
        self.client.send_message("/max_energy", features[0][1])

        self.client.send_message("/centroid", features[1][0])
        self.client.send_message("/max_centroid", features[1][1])
        self.client.send_message("/min_centroid", features[1][2])

        self.client.send_message("/spread", features[2][0])
        self.client.send_message("/max_spread", features[2][1])
        self.client.send_message("/min_spread", features[2][2])
        
        self.client.send_message("/entropy", features[3][0])
        self.client.send_message("/min_entropy", features[3][1])
        self.client.send_message("/max_entropy", features[3][2])

    def send_static(self, feature, address):
        self.client.send_message(address, feature)
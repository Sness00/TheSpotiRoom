## The SpotiRoom
Welcome to the SpotiRoom, enjoy your stay!
![The SpotiRoom](/img/rendering_finale.png)

## Concept
Have you ever felt the same place in different ways according to what music you were listening to at the moment?
This application expresses this very feeling, bringing different sensations to life, playing with light and movement.

Watch as the lights and the background change according to the songs' mood in the moment, while particles dance in a flutter of colors!

## Requirements
<u>**This application runs only on Windows OS.**</u>  

To enjoy the application, follow these instructions: 
- **Access to Spotify Web API**:

    the application needs the credentials of a Spotify App, which you can create [here](https://developer.spotify.com/).

    Take note of your Client ID, Client Secret and Redirect URI, found under the Settings tab, they'll be useful later.

- **Python**: up to 3.11.
    
    It is recommended to create a new virtual environment to host the required packages. After creating one, run the following command:

    ```
    pip install -r requirements.txt
    ```
- **.NET framework**:
    you can install the .NET framework [here](https://dotnet.microsoft.com), or if you want to personalize your scene you can install [vvvv gamma](https://visualprogramming.net/) instead.

## First Run

After satisfying the requirements, do the following.

1. Clone or download the repo content

2. Unpack _the_spotiroom.zip_ inside the folder __the_spotiroom__

3. Run _main.py_

4. Insert Client ID, Client Secret and Redirect URI in the opened window:
![Credentials](/img/credentials.png)

5. A browser tab should open. Copy the link and paste it inside the following window:
![Link](/img/link.png)

6. Sit back and enjoy! Next time you'll run the app it will skip the authentication process and will start to reproduce music automatically

7. You can turn off the application simply by closing Spotify, or by pressing the __Quit App__ button:
![Quit](/img/quit.png)

## Technologies

+ python 3.11:
    - spotipy
    - python-osc
    - numpy
    - scipy
+ vvvv gamma 6.4:
    - VL.Fuse
    - VL.TextureFX

+ blender 4.0
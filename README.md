# Visuafy
Visuafy is a flask based visualiser and remote for Spotify which provides playback controls and different themes to choose from along with a custom theme which allows users to upload their own image as a background.  
  
**Screenshots:**  
  
Gradient Theme:  
![alt text](https://i.ibb.co/0FSbn1G/Gradient.png)  
  
Turntable Theme:  
![alt text](https://i.postimg.cc/WbTQ0DNm/Screenshot-2023-01-13-at-2-47-32-PM.png)  
  
Please note that for the program to work, you would require your own Spotify client ID and secret.  
To do so,  
- open https://developer.spotify.com/dashboard/ , sign in and create an app.  
- Click on 'Edit Settings' and set 'http://127.0.0.1:5000/' as a redirect URI.  
- Finally, paste your Spotify client ID and secret on line 14 and 15 of main.py

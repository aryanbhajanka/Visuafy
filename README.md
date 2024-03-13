# V I S U A F Y
Visuafy is a Flask based visualiser and remote for Spotify which provides playback controls and different themes to choose from along with a custom theme which allows users to upload their own image as a background. Visuafy offers 3 primary themes: gradient, turntable, and custom image, each of which are described below.<br>

## Gradient Theme
Gradient theme is a minimalistic, active gradient of colours, smartly extracted from the current playing song's artwork using the python library, colorthief. The program also decides the best suitable text colour by judging the overall pallet of the artwork such that the text is clearly visible.

![alt text](https://github.com/aryanbhajanka/Visuafy/blob/main/screenshots/gradient.png?raw=true)<br>

## Turntable Theme
Turntable theme, as the name suggests, is an animated vinyl record player where the record has the image of the current playing song's artwork.

![alt text](https://github.com/aryanbhajanka/Visuafy/blob/main/screenshots/turntable.png?raw=true)<br>

## Custom Image
Custom image theme provides users with the option to use any GIF or static image as a background for the visuliser. Visuafy features 12 beautiful GIF images which were specially chosen to make the visualiser feel as aesthetic as possible. The custom image theme also offers two player options, large and small.

Upload Image:
![alt text](https://github.com/aryanbhajanka/Visuafy/blob/main/screenshots/upload_image.png?raw=true)

Large Player:<br>
![alt text](https://github.com/aryanbhajanka/Visuafy/blob/main/screenshots/custom_large.png?raw=true)

Small Player:
![alt text](https://github.com/aryanbhajanka/Visuafy/blob/main/screenshots/custom_small.png?raw=true)<br>

## Other Screenshots
Sign In Page:
![alt text](https://github.com/aryanbhajanka/Visuafy/blob/main/screenshots/sign_in.png?raw=true)

Home Page:
![alt text](https://github.com/aryanbhajanka/Visuafy/blob/main/screenshots/home.png?raw=true)<br>

## Note On Running The Program:
Please note that for the program to work, you would require your own Spotify client ID and secret. To do so,  
- open https://developer.spotify.com/dashboard/ , sign in and create an app.  
- Click on 'Edit Settings' and set 'http://127.0.0.1:5000/' as a redirect URI.  
- Finally, paste your Spotify client ID and secret on line 15 and 16 of main.py

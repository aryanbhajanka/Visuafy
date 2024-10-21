_Spotify is yet to apporve my user quota extension so if you would like to use Visuafy, kindly email me at aryanbhajanka204@gmail.com with your full name as per your Spotify account and registered email address._

# Visuafy
Visuafy is a Flask based visualiser and remote for Spotify which provides playback controls and different themes to choose from along with a custom image theme which allows users to upload their own image as a background. Visuafy offers 3 primary themes: gradient, turntable, and custom image, each of which are shown below.

**Gradient Theme**: A minimalistic, active gradient of colours, smartly extracted from the current playing song's artwork using the python library, colorthief. The program also decides the best suitable text colour by judging the overall pallet of the artwork such that the text is clearly visible.

![alt text](https://i.ibb.co/JcKChNv/gradient.png)
  
**Turntable Theme**: Turntable theme, as the name suggests, is an animated vinyl record player where the record has the image of the current playing song's artwork.

![alt text](https://i.ibb.co/X83vpvV/turntable.png)

**Custom Image Theme**: Custom image theme provides users with the option to use any GIF or static image as a background for the visuliser. Visuafy features 12 beautiful GIF images which were specially chosen to make the visualiser feel as aesthetic as possible. The custom image theme also offers two player options, large and small.

Small:

![alt text](https://i.ibb.co/ws6SFQc/cutom-small.png)

Large:  

![alt text](https://i.ibb.co/fnHKDZF/custom-large.png)

**Uplaod Image Page**:  

![alt text](https://i.ibb.co/K0VMYXc/upload.png)

**Login Page**:  

![alt text](https://i.ibb.co/pWBVLN8/login.png)

**Home Page**:  

![alt text](https://i.ibb.co/ZHh57xV/home.png)  

  
Please note that for the program to work, you would require your own Spotify client ID and secret.  
To do so,  
- open https://developer.spotify.com/dashboard/ , sign in and create an app.  
- Click on 'Edit Settings' and set 'http://127.0.0.1:5000/' as a redirect URI.  
- Finally, paste your Spotify client ID and secret on line 14 and 15 of main.py

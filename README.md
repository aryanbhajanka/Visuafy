*Spotify is yet to apporve my user quota extension so if you would like to use Visuafy, kindly [email me]mailto:aryanbhajanka204@gmail.com with your Spotify username and registered email address. *

# Visuafy
Visuafy is a Flask based visualiser and remote for Spotify which provides playback controls and different themes to choose from along with a custom image theme which allows users to upload their own image as a background. Visuafy offers 3 primary themes: gradient, turntable, and custom image, each of which are shown below.

**Gradient Theme**: A minimalistic, active gradient of colours, smartly extracted from the current playing song's artwork using the python library, colorthief. The program also decides the best suitable text colour by judging the overall pallet of the artwork such that the text is clearly visible.

![alt text](https://media.licdn.com/dms/image/v2/D4D2DAQFYeq1imYr9wA/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1710346542044?e=1729407600&v=beta&t=foVSo3ZZqz-Ny5YKc0vDyt2aPWXOU34au32eF2Xkr-0)  
  
**Turntable Theme**: Turntable theme, as the name suggests, is an animated vinyl record player where the record has the image of the current playing song's artwork.

![alt text](https://media.licdn.com/dms/image/v2/D4D2DAQGID5qa1sY-CA/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1710346564920?e=1729407600&v=beta&t=r199AbyWxbrWIe-oUT0B1CkfHK-xkI68j4Kbld88YAk)

**Custom Image Theme**: Custom image theme provides users with the option to use any GIF or static image as a background for the visuliser. Visuafy features 12 beautiful GIF images which were specially chosen to make the visualiser feel as aesthetic as possible. The custom image theme also offers two player options, large and small.

Small:

![alt text](https://media.licdn.com/dms/image/v2/D4D2DAQF9r23tqW8rZA/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1728750284188?e=1729407600&v=beta&t=_5duRrQfpSmuLD_JSSFbgAGCWyeTc5TOAsvEp5A2nik)

Large:  

![alt text](https://media.licdn.com/dms/image/v2/D4D2DAQFuJl3HTidnlw/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1710346597893?e=1729407600&v=beta&t=GJm7OXmxYQsXfe2Tt_0HQLyFMTo5qykqaOaAxeegp4E)

**Uplaod Image Page**:  

![alt text](https://media.licdn.com/dms/image/v2/D4D2DAQGXZUxQUBJn9g/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1710346519150?e=1729407600&v=beta&t=_mFQgz0Ka9YafAmC2T7mU_9BDrhOPKxcMFc1ns528rU)

**Login Page**:  

![alt text](https://media.licdn.com/dms/image/v2/D4D2DAQGvFGe7QTfOvg/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1710346461533?e=1729407600&v=beta&t=-BHQ8bLk1amd4AZPCkL9BZL3xC4v8Mj9fQiEN3826KA)

**Home Page**:  

![alt text](https://media.licdn.com/dms/image/v2/D4D2DAQESElLnVJ97Ew/profile-treasury-image-shrink_800_800/profile-treasury-image-shrink_800_800/0/1710346491578?e=1729407600&v=beta&t=4Dm1ZAmT_rP2YpCqyxxKkjUpsMzHeSNLNvAqzKyHpsA)  

  
Please note that for the program to work, you would require your own Spotify client ID and secret.  
To do so,  
- open https://developer.spotify.com/dashboard/ , sign in and create an app.  
- Click on 'Edit Settings' and set 'http://127.0.0.1:5000/' as a redirect URI.  
- Finally, paste your Spotify client ID and secret on line 14 and 15 of main.py

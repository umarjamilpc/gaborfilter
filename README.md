**************************************************************************************************************************
NOTES:
**************************************************************************************************************************
Playing a MP3 using a Amazon Alexa (Dot/Echo) device can be somewhat troublesome.
Therefore this quick how to.

Requirements :
A website that has SSL with an official certificate (not Letsencrypt and not a self signed one)
One or more MP3 files that are saved as 48k with a constant bitrate and joint stereo.
With Audacity the save options should look like this.

![Alt text for the image](/audacity.png)

With FFmpeg you should convert your MP3 with the following command:
ffmpeg -i -ac 2 -codec:a libmp3lame -b:a 48k -ar 24000
Or you can convert the MP3 online HERE
Next, upload the converted MP3 to the website and check if you can open it with your browser.

Now with Home Assistant you can test it by going to Developer Tools / Services and in the “Service” field enter notify.alexa_media
In the “Message” field enter : <audio src=’https://automatiseer.eu/audio/kleine-wasjes-grote-wasjes.mp3’/> (change the mp3 to your mp3 or use this one for testing)
Now put the check-mark before “Target” and in the Target Field enter the name of your echo device (i.e. media_player.echo_dot)
Now check-mark the “Data” and in the field enter:
type: tts

So eventually it should look something like this.

![Alt text for the image](/ha_developer_tool.png)

Now hit the “Call Service” button to test it.

**************************************************************************************************************************
TEXT TO SOUND FILE
**************************************************************************************************************************
https://www.narakeet.com/tools/#text-to-audio-online-voice-generator
https://www.getvoila.ai/ai-translate/urdu-to-english

**************************************************************************************************************************
AUDACITY
**************************************************************************************************************************

CHANNELS: STEREO
SAMPLE RATE: 24000 HZ
BIT RATE MODE: CONSTANT
QUALITY: 48 KBPS
EXPORT: ENTIRE PROJECT

CTRL A
EFFECT -> VOLUME & COMPRESSION -> AMPLIFY
NEW PEAK AMPLITUDE (DB): 3 DB
ALLOW CLIPPING

***************************************************************************************************************************
HOME ASSISTANT
***************************************************************************************************************************
DEVELOPER TOOL -> ACTIONS -> Sends a notification message

MESSAGE: <audio src='https://path/to/file/waterpumpurdu2.mp3'/>

DATA: type: tts

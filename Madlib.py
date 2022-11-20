import script1, script2, script3
import pyttsx3, random

voice=pyttsx3.init()
voice_id="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
voice.setProperty('voice',voice_id)
m=random.choice([script1,script2,script3])
voice.say(m.madlib())
voice.runAndWait()
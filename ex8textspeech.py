# from gtts import gTTS
# from threading import Timer 
# from os import system
import win32com.client
data=["ramu","niss","nishi","monika","sanaya"]

speaker=win32com.client.Dispatch("SAPI.SpVoice") #speak names

for name in data:
    speaker.Speak(f'Welcome ,{name}')

# def exec_func(i):
#     mytext = f"Hi {i} , this is an example of converting text to audio. This is a bot speaking here, not a real human!"
#     audio = gTTS(text=mytext, lang="en", slow=False)
#     audio.save("example.mp3")
#     # playsound("example.mp3")
#     os.system("start example.mp3")
 
# for i in data:   
#     Timer(100, exec_func(i)).start()


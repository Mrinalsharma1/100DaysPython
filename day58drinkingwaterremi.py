import win32com.client
import time

def reminder():
    speaker=win32com.client.Dispatch("SAPI.SpVoice") #speak names
    speaker.Speak('stop doing work and drink a ship of water ')

starttime = time.time()
while True:
    print("tick")
    reminder()
    time.sleep(60)
    # time.sleep(60.0 - ((time.time() - starttime) % 60.0))

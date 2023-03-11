import win32com.client
from plyer import notification
import time

def reminder():
    speaker=win32com.client.Dispatch("SAPI.SpVoice") #speak names
    notification.notify(
        title = "General Reminder",
        message = "stop doing work and drink a ship of water",
        timeout = 20
    )
    speaker.Speak('stop doing work and drink a ship of water ')

starttime = time.time()
while True:
    reminder()
    time.sleep(60)
    # time.sleep(60.0 - ((time.time() - starttime) % 60.0))

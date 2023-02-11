from plyer import notification
import time 
import datetime 
if __name__=='__main__':
  while True:
    now = datetime.datetime.now()
    notification.notify(
    title="*** Take Rest ****",
    message=f"""Please Take a break. You have been working for a half an hour. The current time is {now.strftime("%H:%M:%S")}""",
    app_icon="D:/wstube/python/try.ico",
    timeout=5)
    time.sleep(1800)
#pythonw filename.py-To run python in background
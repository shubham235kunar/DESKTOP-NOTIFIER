import time
from plyer import notification 
if __name__=="__main__":
    while True:
        notification.notify(
            title ="have some water BUDDY!!!",
            message="maintain your Blood Pressure",
            timeout=3
        )
        time.sleep(11)
        

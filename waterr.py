import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Drink Water Now!",
            message="It is recommended to drink 8 glasses of water per day.",
            app_name="Water Drinking Reminder",
            timeout=5
        )
        # notification will be sent every 30 minutes
        time.sleep(30*60)





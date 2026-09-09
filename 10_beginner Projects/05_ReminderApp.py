import time
from plyer import notification

while True:
    print("Reminder: Take a sip of water!")
    # to get notification.
    notification.notify(
        title="Water Reminder",
        message="It's time to drink some water!",
        timeout=10
    )
    time.sleep(1800)  # Wait for 30 min before reminding again


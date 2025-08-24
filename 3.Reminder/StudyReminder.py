import time
from datetime import datetime
from plyer import notification

def daily_remind():
    while True: 
        present = datetime.now()
        hour = present.hour
        minute = present.minute

        if hour >= 22:
            print("Done for today! See you tomorrow for more studies.")
            break

        if (hour, minute) == (21, 0):
            print("Completed 2 hour study session")
            notification.notify(title="Dinner Break",
                message="It's 9:00 PM — Take a break and enjoy your dinner!",
                timeout=10
            )
            time.sleep(60)

 
        elif (hour, minute) in [(19, 0), (20, 0), (21, 30)]:
            notification.notify(
                title="Study Reminder",
                message="Time to focus on your studies!",
                timeout=10
            )
            time.sleep(60)

        time.sleep(20)  

        print("Good job, will restart reminders tomorrow at 7 PM.")

        present = datetime.now()
        wait_seconds = ((24 - present.hour + 19) * 3600) - present.minute * 60 - present.second
        time.sleep(wait_seconds)


if __name__ == "__main__":
    print("Reminders active (7 PM, 8 PM, 9 PM Dinner, 9:30 PM Again Study or Revise).")
    daily_remind()
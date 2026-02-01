from win10toast import ToastNotifier
import time

def show_motto():
    toaster = ToastNotifier()
    
    # Your Mission Statement
    title = "Lee Automation: Mission Active"
    message = "I am a steward of my time. I build for my family. I code for freedom."
    
    # This shows the notification for 10 seconds
    toaster.show_toast(
        title,
        message,
        duration=10,
        threaded=True
    )

if __name__ == "__main__":
    # Small delay to let Windows finish loading before the pop-up appears
    time.sleep(5) 
    show_motto()
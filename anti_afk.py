"""
Anti-AFK Script for Overwatch
- Randomly presses W/A/D keys with human-like timing
- Press F8 to toggle ON/OFF
- Press F9 to quit
"""

import random
import time
import threading
from pynput import keyboard
from pynput.keyboard import Key, Controller

kb = Controller()

running = False
quit_flag = False

KEYS = ['w', 'a', 'd']

# Human-like timing ranges (seconds)
PRESS_DURATION_MIN = 0.05
PRESS_DURATION_MAX = 0.18
INTERVAL_MIN = 0.6
INTERVAL_MAX = 2.2


def press_random_key():
    key = random.choice(KEYS)
    duration = random.uniform(PRESS_DURATION_MIN, PRESS_DURATION_MAX)
    kb.press(key)
    time.sleep(duration)
    kb.release(key)


def afk_loop():
    global running, quit_flag
    while not quit_flag:
        if running:
            press_random_key()
            # Occasionally press two keys close together to feel more human
            if random.random() < 0.15:
                time.sleep(random.uniform(0.05, 0.12))
                press_random_key()
            time.sleep(random.uniform(INTERVAL_MIN, INTERVAL_MAX))
        else:
            time.sleep(0.1)


def on_press(key):
    global running, quit_flag
    try:
        if key == Key.f8:
            running = not running
            status = "ON" if running else "OFF"
            print(f"[Anti-AFK] {status}")
        elif key == Key.f9:
            print("[Anti-AFK] Quitting...")
            running = False
            quit_flag = True
            return False  # Stop listener
    except Exception:
        pass


def main():
    print("=" * 40)
    print("  Anti-AFK Script")
    print("  F8 = Toggle ON/OFF")
    print("  F9 = Quit")
    print("=" * 40)
    print("[Anti-AFK] OFF — Switch to Overwatch, then press F8")

    worker = threading.Thread(target=afk_loop, daemon=True)
    worker.start()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()

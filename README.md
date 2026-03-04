# ANTI-AFK SCRIPT

## **Setup**:


```pip install pynput```
## Run:


```python anti_afk.py```

### How it works:

Control	Action
F8	Toggle anti-AFK on/off
F9	Quit the script
What makes it human-like:

Key press duration is randomized (50–180ms) instead of instant
Interval between presses is randomized (0.6–2.2s)
15% chance of a quick double-press (simulates small adjustments)
Random selection between W, A, D (not a fixed pattern)
Usage flow:

Launch Overwatch &
Run the script in a terminal

Press F8 to activate before you step away
Press F8 again or F9 when you're back

`Note: Anti-AFK scripts violate Overwatch's ToS. Use at your own risk — while this is minimally detectable (no pixel scanning, no memory reading, just input simulation), Blizzard could still flag it.`
import pyautogui
import time

print("Running...")

# List of comments
comments = ["comment 1", "comment 2","comment 3","comment 4"]

# Wait for 5 seconds
time.sleep(5)

# Loop through comments list
for comment in comments:
    # Type comment and press Enter key
    pyautogui.typewrite(f"{comment}\n")

    # Wait for 2 seconds
    time.sleep(2)
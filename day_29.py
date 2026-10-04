# Day 29: Introduction to GUI Automation

import pyautogui
import time

print("--- GUI Automation Script Initialized ---")

# 1. Getting Screen Size
screen_width, screen_height = pyautogui.size()
print(f"Screen Resolution Detected -> Width: {screen_width}, Height: {screen_height}")

# 2. Safety pause
pyautogui.PAUSE = 1.0

# 3. Simulating Mouse Movement (Moving mouse to screen center smoothly)
print("Moving mouse to the center of the screen...")
pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=1.5)

print("\nGUI Automation concepts successfully tested!")
print("Note: In real-world AI GUI tasks, visual object detection is used to locate and click buttons automatically.")
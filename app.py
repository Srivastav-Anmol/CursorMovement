import pyautogui
import random
import time

def main():
    print("Script is active")
    while True:
        time.sleep(5)  # Sleep for 5 seconds
        # Assuming you have 640 * 480 resolution laptop screen
        x = random.randint(0, 639)  
        y = random.randint(0, 479) 
        print(f"{x} , {y}")
        pyautogui.moveTo(x, y) 
main()

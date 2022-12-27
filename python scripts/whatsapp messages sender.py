import pyautogui as gui
import time
# whatsapp message sender 
number = input("how many times you want to send the message")
message = input("Enter the message you want to send")
print("locate the cursor to the input box")

time.sleep(5)

for i in range(int(number)):

  gui.typewrite(message)
  gui.press("Enter")


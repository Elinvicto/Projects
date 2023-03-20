#Edit message before running program
import pyautogui as pg 
import webbrowser as wb
import time
wb.open("https://web.whatsapp.com/") #Delivery website
time.sleep(0.01) #Timer
for i in range(200): #Number of messages
    pg.write("Just for Prank 😜😜") #Message Content
    time.sleep(0.01) 
    pg.press("Enter")

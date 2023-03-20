import pyautogui as pg 
import webbrowser as wb
import time
wb.open("https://web.whatsapp.com/")
time.sleep(0.01)
for i in range(200):
    pg.write("nahi jat")
    time.sleep(0.01)
    pg.press("Enter")
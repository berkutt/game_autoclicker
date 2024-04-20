import pyautogui
import time
# pyautogui.position()

place_1 = (2713, 542)
place_2 = (2636, 485)
place_3 = (2541, 432)
place_4 = (2806, 482)
place_5 = (2710, 436)
place_6 = (2630, 378)
place_7 = (2900, 434)
place_8 = (2809, 381)
place_9 = (2715, 336)


while True:
    # harvest
    for i in range(0,10):
        pyautogui.click(place_1)
    pyautogui.click(place_2)
    pyautogui.click(place_3)
    pyautogui.click(place_4)
    pyautogui.click(place_5)
    pyautogui.click(place_6)
    pyautogui.click(place_7)
    pyautogui.click(place_8)
    pyautogui.click(place_9)

    # upgrade fruit
    #open shop
    pyautogui.click(2237, 668)
    #click upgrade
    time.sleep(1)
    pyautogui.click(2734, 355)
    time.sleep(1)
    # close shop
    pyautogui.click(2844, 266)
    time.sleep(1)

    # upgrade place
    pyautogui.click(2305, 663)
    # time.sleep(1)
    pyautogui.click(place_1)
    pyautogui.click(place_2)
    pyautogui.click(place_3)
    pyautogui.click(place_4)
    pyautogui.click(place_5)
    pyautogui.click(place_6)
    pyautogui.click(place_7)
    pyautogui.click(place_8)
    pyautogui.click(place_9)
    # close upgrade mode
    
    pyautogui.click(2305, 663)

    # time.sleep(10)

    pyautogui.position()
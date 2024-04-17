import pyautogui
import time

# pyautogui.position()
time.sleep(2)
for i in range(0,2000):
     
    if i%2==0:
        print("upgrade storage")
        # storage upgrade
        pyautogui.click(2333, 443)
        time.sleep(1)
        for j in range(0,20):
            pyautogui.click(2535, 384)
            pyautogui.click(2535, 384)

    # if i%2==0:
    #     print("upgrade kiwi")
    #     #kiwi upgrade
    #     pyautogui.click(2723, 653)
    #     pyautogui.click(2723, 653)
    #     time.sleep(1)
    #     for j in range(0,20):
    #         pyautogui.click(2821, 589)
    #         pyautogui.click(2821, 589)

    print("Boosting")
    for j in range(0,100):
        # click farm boost
        pyautogui.click(2717, 334)

    print("Clicking kiwi")
    for j in range(0,10):
        # click kiwi
        pyautogui.click(2722,577)

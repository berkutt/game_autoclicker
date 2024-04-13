import pyautogui
import time
pyautogui.position()
# Define the coordinates where the click will happen. 
# You can get the coordinates using pyautogui.position() function in Python shell\

class MinerFarm:
    class Mine:
        def __init__(self, human, lvl_up):
            self.human = human
            self.lvl_up = lvl_up

    class Elevator:
        def __init__(self, human, lvl_up):
            self.human = human
            self.lvl_up = lvl_up

    class Transporter:
        def __init__(self, human, lvl_up):
            self.human = human
            self.lvl_up = lvl_up

    class Lvl_up_btn:
        def __init__(self, lvl_up, close):
            self.lvl_up = lvl_up
            self.close = close
    
    class View_level_up:
        def __init__(self, lvl_up):
            self.lvl_up = lvl_up

mine = MinerFarm.Mine((2710, 649),(2910, 630))
elevator = MinerFarm.Elevator((2498, 505),(2500, 290))
transporter = MinerFarm.Transporter((2866, 410),(2915, 304))
button_upgrade = MinerFarm.Lvl_up_btn((2802, 530), (2883, 249))
level_view_up = MinerFarm.View_level_up((2247, 233))

def mine_upgrade():
    pyautogui.click(mine.lvl_up)
    time.sleep(1)
    pyautogui.click(button_upgrade.lvl_up)
    time.sleep(1)
    pyautogui.click(button_upgrade.close)
    time.sleep(1)

def transporter_upgrade():
    pyautogui.click(transporter.lvl_up)
    time.sleep(1)
    pyautogui.click(button_upgrade.lvl_up)
    time.sleep(1)
    pyautogui.click(button_upgrade.close)
    time.sleep(1)

def elevator_upgrade():
    pyautogui.click(elevator.lvl_up)
    time.sleep(1)
    pyautogui.click(button_upgrade.lvl_up)
    time.sleep(1)
    pyautogui.click(button_upgrade.close)
    time.sleep(1)

def view_level_up():
    pyautogui.click(level_view_up.lvl_up)
    time.sleep(0.5)
    pyautogui.click(level_view_up.lvl_up)
    time.sleep(0.5)
    pyautogui.click(level_view_up.lvl_up)
    time.sleep(0.5)

while True:

    for i in range(0,500):
        mine_upgrade()

    transporter_upgrade()

    view_level_up()


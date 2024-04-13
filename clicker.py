import pyautogui
import time

from screenshot_reader import get_capacity
# pyautogui.position()

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

    class View_level_down:
        def __init__(self, lvl_down):
            self.lvl_down = lvl_down

mine = MinerFarm.Mine(human=(2710, 649),lvl_up=(2910, 630))
elevator = MinerFarm.Elevator(human=(2498, 505),lvl_up=(2500, 290))
transporter = MinerFarm.Transporter(human=(2866, 410),lvl_up=(2915, 304))
button_upgrade = MinerFarm.Lvl_up_btn(lvl_up=(2802, 530), close=(2883, 249))
level_view_up = MinerFarm.View_level_up(lvl_up=(2247, 233))
level_view_down = MinerFarm.View_level_down(lvl_down=(2247, 328))

def mine_upgrade():
    print("mine")
    pyautogui.click(mine.lvl_up)
    time.sleep(1)
    capacity = get_capacity()
    pyautogui.click(button_upgrade.lvl_up)
    time.sleep(1)
    pyautogui.click(button_upgrade.close)
    time.sleep(1)
    return capacity

def transporter_upgrade():
    print("transporter")
    pyautogui.click(transporter.lvl_up)
    time.sleep(1)
    capacity = get_capacity()
    pyautogui.click(button_upgrade.lvl_up)
    time.sleep(1)
    pyautogui.click(button_upgrade.close)
    time.sleep(1)
    return capacity

def elevator_upgrade():
    print("elevator")
    pyautogui.click(elevator.lvl_up)
    time.sleep(1)
    capacity = get_capacity()
    pyautogui.click(button_upgrade.lvl_up)
    time.sleep(1)
    pyautogui.click(button_upgrade.close)
    time.sleep(1)
    return capacity

def view_level_up():
    print("gowing up")
    for i in range(0,4):
        pyautogui.click(level_view_up.lvl_up)
        time.sleep(0.5)

def view_level_down():
    print("going down")
    for i in range(0,4):
        pyautogui.click(level_view_down.lvl_down)
        time.sleep(0.5)

mine_capacity = {'transport_capacity':0,
'elevator_capacity':0,
'miner_capacity':0
}
time.sleep(2)
while True:
    if mine_capacity['transport_capacity']==0:
        view_level_down()
        mine_capacity['miner_capacity'] = mine_upgrade()
        view_level_up()
        mine_capacity['transport_capacity'] = transporter_upgrade()
        mine_capacity['elevator_capacity']= elevator_upgrade()
    else:
        print(mine_capacity)
        upgrade_target = min(mine_capacity, key=mine_capacity.get)
        print(f"it's time to upgrade {upgrade_target}")  
        if upgrade_target == 'miner_capacity':
            view_level_down()
            mine_capacity['miner_capacity'] = mine_upgrade()
        if upgrade_target == 'transport_capacity':
            view_level_up()
            mine_capacity['transport_capacity'] = transporter_upgrade()
        if upgrade_target == 'elevator_capacity':
            view_level_up()
            mine_capacity['elevator_capacity']= elevator_upgrade()

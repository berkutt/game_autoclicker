import pyautogui
import time
from PIL import ImageGrab

# Constants
NEW_LVL_COORDINATES = (1564, 43)
RIGHT_TO_LAST_LVL_COORDINATES = (1573, 37)
PREVIOUS_LVL_COORDINATES = (1351,70)
MINION_MAIN_COORDINATES = (1443, 579)
HERO_UPDATE_START_COORDINATES = (88, 407)
HERO_UPDATE_END_COORDINATES = (682, 929)
ABILITY_START_COORDINATES = (1000, 301)
ABILITY_END_COORDINATES = (1000, 988)
BUTTON_DOWN_COORDINATES = (877, 1059)
BUTTON_UP_COORDINATES = (877, 396)
BOSS_LVL_COORDINATES = (1399, 237)
CLOSE_SHOP_COORDINATES = (1777,82)

ABILITY_1_COORDINATES = (1013,310)
ABILITY_2_COORDINATES = (1013,386)
ABILITY_3_COORDINATES = (1013,470)
ABILITY_4_COORDINATES = (1013,561)
ABILITY_5_COORDINATES = (1013,647)
# ABILITY_6_COORDINATES = (1013,652) # USELESS 8 HR COLDOWN
ABILITY_7_COORDINATES = (1013,827) 
ABILITY_8_COORDINATES = (1003,909)
ABILITY_9_COORDINATES = (1013,999)

AUTO_LVL_JUMP = (1879,327)
RGB_DIFF_THRESHOLD = 10
STEP_SIZE = 50
SCROLL_DOWN_TIMES = 100
SCROLL_UP_TIMES = 18

def get_rgb(coordinates):
    """Get RGB value of a pixel at given coordinates."""
    screenshot = pyautogui.screenshot()
    rgb = screenshot.getpixel(coordinates)
    return rgb

def find_pixel_in_screenshot(target_rgb):
    screenshot = pyautogui.screenshot()
    width, height = screenshot.size

    for y in range(height):
        for x in range(width):
            r, g, b = screenshot.getpixel((x, y))
            if (r, g, b) == target_rgb:
                return True, (x, y)

    return False, None

# Use the function
target_rgb = (167, 206, 55)
found, position = find_pixel_in_screenshot(target_rgb)
class GameActions:
    """Class to perform game actions."""

    def __init__(self):
        """Initialize coordinates."""
        self.new_lvl_coordinates = NEW_LVL_COORDINATES
        self.right_to_last_lvl_coordinates = RIGHT_TO_LAST_LVL_COORDINATES
        self.previous_lvl_coordinates = PREVIOUS_LVL_COORDINATES
        self.minion_main_coordinates = MINION_MAIN_COORDINATES
        self.hero_update_start_coordinates = HERO_UPDATE_START_COORDINATES
        self.hero_update_end_coordinates = HERO_UPDATE_END_COORDINATES
        self.ability_start_coordinates = ABILITY_START_COORDINATES
        self.ability_end_coordinates = ABILITY_END_COORDINATES
        self.button_down_coordinates = BUTTON_DOWN_COORDINATES
        self.button_up_coordinates = BUTTON_UP_COORDINATES
        self.boss_lvl_coordinates = BOSS_LVL_COORDINATES
        self.close_shop_coordinates = CLOSE_SHOP_COORDINATES

        self.ability_1_coordinates = ABILITY_1_COORDINATES
        self.ability_2_coordinates = ABILITY_2_COORDINATES
        self.ability_3_coordinates = ABILITY_3_COORDINATES
        self.ability_4_coordinates = ABILITY_4_COORDINATES
        self.ability_5_coordinates = ABILITY_5_COORDINATES
        self.ability_7_coordinates = ABILITY_7_COORDINATES
        self.ability_8_coordinates = ABILITY_8_COORDINATES
        self.ability_9_coordinates = ABILITY_9_COORDINATES

        self.auto_lvl_jump_coordinates = AUTO_LVL_JUMP

    def click(self, coordinates, safe=True):
        """Click at given coordinates."""
        pyautogui.click(*coordinates)
        
        if safe: 
            time.sleep(0.2)
            pyautogui.mouseUp(self.minion_main_coordinates)

    def click_new_lvl(self):
        print("Go to new lvl")
        """Click at new level coordinates."""
        self.click(self.new_lvl_coordinates)
        time.sleep(0.5)

    def click_previous_lvl(self):
        print('lvl back')
        self.click(self.previous_lvl_coordinates)
        time.sleep(0.5)

    def check_lvl_update(self):
        """Check if level update is available."""
        diff = abs(sum(get_rgb(self.right_to_last_lvl_coordinates)) - 
                   sum(get_rgb(self.new_lvl_coordinates)))
        return diff > RGB_DIFF_THRESHOLD

    def click_minion_main(self):
        """Click at minion main coordinates."""
        self.click(self.minion_main_coordinates, safe=False)

    def lvl_up_hero(self):
        print("Time for update")
        """Level up hero."""
        # self.scroll_down()
        for i in range(2):
            self.click_everywhere()
            self.scroll_up()
            if i == 0:
                pyautogui.press('t') # x10 purchase
        self.click_everywhere()
        # reset purchase
        pyautogui.press('t')
        pyautogui.press('t')
        pyautogui.press('t')
        pyautogui.press('t')
        self.scroll_down()
        

    def click_everywhere(self):
        """Click everywhere in the hero update area."""
        x_steps = (self.hero_update_end_coordinates[0] - self.hero_update_start_coordinates[0]) // STEP_SIZE
        y_steps = (self.hero_update_end_coordinates[1] - self.hero_update_start_coordinates[1]) // STEP_SIZE

        for i in range(x_steps):
            for j in range(y_steps):
                x = self.hero_update_end_coordinates[0] - i * STEP_SIZE
                y = self.hero_update_end_coordinates[1] - j * STEP_SIZE
                self.click((x, y))
                self.click((1456, 150)) # close window about assend
                # self.click(self.close_shop_coordinates)

    def scroll_down(self, SCROLL_DOWN_TIMES=SCROLL_DOWN_TIMES):
        """Scroll to next hero."""
        for _ in range(SCROLL_DOWN_TIMES):
            self.click(self.button_down_coordinates)
    
    def scroll_up(self):
        """Scroll back to top."""
        for _ in range(SCROLL_UP_TIMES):
            self.click(self.button_up_coordinates)

    def is_boss_lvl(self):
        
        """Check if current level is a boss level."""
        return sum(get_rgb(self.boss_lvl_coordinates)) == 275

    def click_abilities(self):
        print("Turning on abilities")
        # x = self.ability_start_coordinates[0]
        # for j in range(9):
        #     time.sleep(0.2)
        #     y = self.ability_start_coordinates[1] + j * 96
        #     self.click((x, y))
        self.click((self.ability_9_coordinates))
        self.click((self.ability_8_coordinates))
        self.click((self.ability_3_coordinates))
        self.click((self.ability_1_coordinates))
        self.click((self.ability_2_coordinates))
        self.click((self.ability_7_coordinates))
            

time.sleep(2)
game = GameActions()


def boss_fight():
        print("***BOSS***")
        time.sleep(0.5)
        game.click_previous_lvl()
        game.lvl_up_hero()
        game.click_new_lvl()
        game.click_abilities()
        click_auto_lvl()
        for _ in range(350):
            game.click_minion_main()

def farm_gold():
    print("***FARM***")
    game.click_previous_lvl()
    if game.is_boss_lvl(): farm_gold() # if clicked didn't work, use recursion
    game.click((game.ability_4_coordinates))
    game.click((game.ability_5_coordinates)) 

    for farm_round in range(15):
        print(f"{farm_round}")
        if game.is_boss_lvl(): farm_gold() 
        for _ in range(400):
            game.click_minion_main()

def clean_window():
    game.click((946, 553)) # open chest
    
    time.sleep(1)
    game.click((1493, 187)) # close window
    
    game.click((829, 648)) # destroy relics from junk
    time.sleep(1)
    game.click((1462, 152)) # close window about assend

def click_auto_lvl(unclick=False):
    # check if auto-play is off rgb(253, 0, 23)
    if unclick:
            if sum(get_rgb(game.auto_lvl_jump_coordinates)) != 276:
                print("Unclicking auto-lvl")
                game.click(game.auto_lvl_jump_coordinates)
                time.sleep(0.2)
                click_auto_lvl(True) # need to make sure that it clicked
            else:
                return
    else:   
        if sum(get_rgb(game.auto_lvl_jump_coordinates)) == 276:
            print("Clicking auto-lvl")
            game.click(game.auto_lvl_jump_coordinates)
            time.sleep(0.2)
            click_auto_lvl() # need to make sure that it clicked
        else:
            return
        
start_time = 0
end_time = 0        

while True:
    # clean_window()

    # game.click_new_lvl()
    click_auto_lvl()

    boss_lvl = game.is_boss_lvl()
    if not boss_lvl:
        game.scroll_down(5)
        game.click((184, 703)) # click on lates hero

    if boss_lvl: 
        start_time = time.time()
    else:
        start_time = 0
        end_time = 0

    for i in range(1,40):
        if  boss_lvl and end_time==0:
            print("Boss fight started")
            click_auto_lvl(unclick=True) 
            end_time = time.time()
        if not boss_lvl:
            end_time = 0
        
        # if not boss lvl, or trtying to earn some gold - try to break, and go next lvl every 20 steps
        if boss_lvl and start_time - end_time>60 and start_time - end_time<500:  
            # failed to kill the boss. Start the "boss fight"
            boss_fight()
            game.click_new_lvl() # is after figgt, new lvl available ? 
            if game.is_boss_lvl(): 
                farm_gold()
            break
        
        game.click_minion_main()
    
    # end_time = time.time()
    # execution_time = end_time - start_time
    # print(f"The function executed in {execution_time} seconds")

    # Point(x=946, y=553) - open chest
    # Point(x=1493, y=187) - close window
import pyautogui
import time

class GameActions:
    """Class to perform game actions."""
    
    # Constants
    NEW_LVL_COORDINATES = (1564, 43)
    RIGHT_TO_LAST_LVL_COORDINATES = (1573, 37)
    PREVIOUS_LVL_COORDINATES = (1351, 70)
    MINION_MAIN_COORDINATES = (1443, 579)
    HERO_UPDATE_START_COORDINATES = (88, 407)
    HERO_UPDATE_END_COORDINATES = (682, 929)
    ABILITY_START_COORDINATES = (1000, 301)
    ABILITY_END_COORDINATES = (1000, 988)
    BUTTON_DOWN_COORDINATES = (877, 1059)
    BUTTON_UP_COORDINATES = (877, 396)
    BOSS_LVL_COORDINATES = (1399, 237)
    CLOSE_SHOP_COORDINATES = (1777, 82)

    ABILITY_COORDINATES = {
        1: (1013, 310),
        2: (1013, 386),
        3: (1013, 470),
        4: (1013, 561),
        5: (1013, 647),
        7: (1013, 827),
        8: (1003, 909),
        9: (1013, 999)
    }

    AUTO_LVL_JUMP_COORDINATES = (1879, 327)
    RGB_DIFF_THRESHOLD = 10
    STEP_SIZE = 50
    SCROLL_DOWN_TIMES = 100
    SCROLL_UP_TIMES = 18

    def __init__(self):
        """Initialize coordinates."""
        self._screenshot = None

    def _get_rgb(self, coordinates):
        """Get RGB value of a pixel at given coordinates."""
        if self._screenshot is None:
            self._screenshot = pyautogui.screenshot()
        return self._screenshot.getpixel(coordinates)

    def _click(self, coordinates, safe=True):
        """Click at given coordinates."""
        pyautogui.click(*coordinates, clicks=2)
        if safe:
            pass
            # pyautogui.mouseUp(self.MINION_MAIN_COORDINATES)

    def click_new_lvl(self):
        """Click at new level coordinates."""
        self._click(self.NEW_LVL_COORDINATES)
        time.sleep(0.5)

    def click_previous_lvl(self):
        """Click at previous level coordinates."""
        self._click(self.PREVIOUS_LVL_COORDINATES)
        time.sleep(0.5)

    def check_lvl_update(self):
        """Check if level update is available."""
        diff = abs(sum(self._get_rgb(self.RIGHT_TO_LAST_LVL_COORDINATES)) - 
                   sum(self._get_rgb(self.NEW_LVL_COORDINATES)))
        return diff > self.RGB_DIFF_THRESHOLD

    def click_minion_main(self):
        """Click at minion main coordinates."""
        self._click(self.MINION_MAIN_COORDINATES, safe=False)

    def lvl_up_hero(self):
        """Level up hero."""
        for i in range(2):
            self._click_everywhere()
            self.scroll_up()
            if i == 0:
                pyautogui.press('t')  # x10 purchase
        self._click_everywhere()
        pyautogui.press('t')  # reset purchase
        pyautogui.press('t')
        pyautogui.press('t')
        pyautogui.press('t')
        self.scroll_down()

    def _click_everywhere(self):
        """Click everywhere in the hero update area."""
        x_steps = (self.HERO_UPDATE_END_COORDINATES[0] - self.HERO_UPDATE_START_COORDINATES[0]) // self.STEP_SIZE
        y_steps = (self.HERO_UPDATE_END_COORDINATES[1] - self.HERO_UPDATE_START_COORDINATES[1]) // self.STEP_SIZE

        for i in range(x_steps):
            for j in range(y_steps):
                x = self.HERO_UPDATE_END_COORDINATES[0] - i * self.STEP_SIZE
                y = self.HERO_UPDATE_END_COORDINATES[1] - j * self.STEP_SIZE
                self._click((x, y), safe=False)
                self._click((1456, 150))  # close window about ascend

    def scroll_down(self):
        """Scroll to next hero."""
        for _ in range(self.SCROLL_DOWN_TIMES):
            self._click(self.BUTTON_DOWN_COORDINATES, safe=False)
    
    def scroll_up(self):
        """Scroll back to top."""
        for _ in range(self.SCROLL_UP_TIMES):
            self._click(self.BUTTON_UP_COORDINATES, safe=False)

    def is_boss_lvl(self):
        """Check if current level is a boss level."""
        return sum(self._get_rgb(self.BOSS_LVL_COORDINATES)) == 275

    def click_abilities(self):
        """Turning on abilities"""
        for ability_coord in self.ABILITY_COORDINATES.values():
            self._click(ability_coord)

    def find_pixel_in_screenshot(self, target_rgb):
        """Find a pixel with a specific RGB value in the screenshot."""
        width, height = self._screenshot.size
        for y in range(height):
            for x in range(width):
                r, g, b = self._screenshot.getpixel((x, y))
                if (r, g, b) == target_rgb:
                    return True, (x, y)
        return False, None

game = GameActions()

def boss_fight():
    """Perform actions for boss fight."""
    game.click_previous_lvl()
    game.click_new_lvl()
    game.click_abilities()
    click_auto_lvl()
    for _ in range(350):
        game.click_minion_main()

def farm_gold():
    """Farm gold."""
    game.click_previous_lvl()
    if game.is_boss_lvl():
        farm_gold()  # if clicked didn't work, use recursion
    game._click(game.ABILITY_COORDINATES[4])
    game._click(game.ABILITY_COORDINATES[5])
    for _ in range(15):
        if game.is_boss_lvl():
            farm_gold()
        for _ in range(400):
            game.click_minion_main()

def clean_window():
    """Clean window."""
    game._click((946, 553))  # open chest
    time.sleep(1)
    game._click((1493, 187))  # close window
    game._click((829, 648))  # destroy relics from junk
    time.sleep(1)
    game._click((1462, 152))  # close window about ascend

def click_auto_lvl(unclick=False):
    """Click auto level."""
    if unclick:
        if sum(game._get_rgb(game.AUTO_LVL_JUMP_COORDINATES)) != 276:
            game._click(game.AUTO_LVL_JUMP_COORDINATES)
            time.sleep(0.2)
            click_auto_lvl(True)
        else:
            return
    else:   
        if sum(game._get_rgb(game.AUTO_LVL_JUMP_COORDINATES)) == 276:
            game._click(game.AUTO_LVL_JUMP_COORDINATES)
            time.sleep(0.2)
            click_auto_lvl()
        else:
            return

start_time = 0
end_time = 0        

while True:
    clean_window()
    boss_lvl = game.is_boss_lvl()
    if not boss_lvl and end_time == 0:
        game.scroll_down(5)
        game._click((184, 703), False)  # click on latest hero
        game._click((646, 1005), False)  # click on latest hero
        start_time = 0
        click_auto_lvl()
    elif not boss_lvl:
        end_time = 0
    else:
        start_time = time.time()
        
    for i in range(1, 200):
        if boss_lvl and end_time == 0:
            click_auto_lvl(unclick=True) 
            end_time = time.time()

        if boss_lvl and 30 < start_time - end_time < 500:
            game.click_new_lvl()
            time.sleep(1)
            if game.is_boss_lvl():
                boss_fight()
                game.click_new_lvl()
                end_time = 0
                if game.is_boss_lvl(): 
                    pass
                    # farm_gold()
                break
        
        game.click_minion_main()

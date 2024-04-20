import pyautogui
import time
from PIL import ImageGrab

# Constants
NEW_LVL_COORDINATES = (1530, 72)
RIGHT_TO_LAST_LVL_COORDINATES = (1641, 73)
PREVIOUS_LVL_COORDINATES = (1351,70)
MINION_MAIN_COORDINATES = (1443, 579)
HERO_UPDATE_START_COORDINATES = (88, 407)
HERO_UPDATE_END_COORDINATES = (682, 989)
ABILITY_START_COORDINATES = (1000, 301)
ABILITY_END_COORDINATES = (1000, 988)
BUTTON_DOWN_COORDINATES = (877, 1059)
BUTTON_UP_COORDINATES = (877, 396)
BOSS_LVL_COORDINATES = (1399, 237)

RGB_DIFF_THRESHOLD = 100
STEP_SIZE = 50
SCROLL_DOWN_TIMES = 100
SCROLL_UP_TIMES = 18

def get_rgb(coordinates):
    """Get RGB value of a pixel at given coordinates."""
    screenshot = pyautogui.screenshot()
    rgb = screenshot.getpixel(coordinates)
    return rgb

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

    def click(self, coordinates):
        """Click at given coordinates."""
        pyautogui.click(*coordinates)

    def click_new_lvl(self):
        print("Go to new lvl")
        """Click at new level coordinates."""
        self.click(self.new_lvl_coordinates)

    def click_previous_lvl(self):
        self.click(self.previous_lvl_coordinates)

    def check_lvl_update(self):
        """Check if level update is available."""
        diff = abs(sum(get_rgb(self.right_to_last_lvl_coordinates)) - 
                   sum(get_rgb(self.new_lvl_coordinates)))
        return diff > RGB_DIFF_THRESHOLD

    def click_minion_main(self):
        """Click at minion main coordinates."""
        self.click(self.minion_main_coordinates)

    def lvl_up_hero(self):
        print("Time for update")
        """Level up hero."""
        # self.scroll_down()
        for _ in range(2):
            self.click_everywhere()
            self.scroll_up()
        self.scroll_down()
        

    def click_everywhere(self):
        """Click everywhere in the hero update area."""
        x_steps = (self.hero_update_end_coordinates[0] - self.hero_update_start_coordinates[0]) // STEP_SIZE
        y_steps = (self.hero_update_end_coordinates[1] - self.hero_update_start_coordinates[1]) // STEP_SIZE

        for i in range(x_steps, -1, -1):
            for j in range(y_steps, -1, -1):
                x = self.hero_update_end_coordinates[0] - i * STEP_SIZE
                y = self.hero_update_end_coordinates[1] - j * STEP_SIZE
                self.click((x, y))

    def scroll_down(self):
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
        x = self.ability_start_coordinates[0]
        for j in range(9):
            y = self.ability_start_coordinates[1] + j * 76
            self.click((x, y))

time.sleep(2)
game = GameActions()


while True:
    if game.check_lvl_update():
        # game.lvl_up_hero()
        game.click_new_lvl()

    if game.is_boss_lvl():
        print("***BOSS***")
        game.click_previous_lvl()
        game.lvl_up_hero()
        game.click_new_lvl()
        game.click_abilities()


    for i in range(1,200):
        print(f"click {i=}")
        if i % 20 == 0 and game.check_lvl_update():
            print("New LVL available")
            break
        game.click_minion_main()

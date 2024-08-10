import os
import tempfile

START_ROOM = "roomOne"

# Add debug level option
DEBUG_LEVEL = "DEBUG"  # Can be "DEBUG", "INFO", "WARNING", "ERROR", or "CRITICAL"
#### CHANGE ME FOR RELEASE ####

# Add log file path in temporary folder
LOG_FILE = os.path.join(tempfile.gettempdir(), "dungeon_game.log")
# Log files will be at C:\Users\<username>\AppData\Local\Temp\dungeon_game.log

# Show where the log file is in the terminal
print(f"Log file is located at: {LOG_FILE}")

# Add the path of quotes.json file
QUOTES_PATH = "src/quotes.json"

ROOM_POSITION = {
    'roomOne': (50, 200),
    'roomTwo': (50, 50),
    'roomThree': (50, 350),
    'roomFour': (200, 350),
    'roomFive': (200, 200),
    'roomSix': (200, 50),
    'roomSeven': (350, 50),
    'roomEight': (350, 200)
}

ROOMS = {
    'roomOne': {'North': 'roomTwo', 'South': 'roomThree', 'East': 'roomFive'},
    'roomTwo': {'South': 'roomOne', 'Item': 'One'},
    'roomThree': {'North': 'roomOne', 'East': 'roomFour', 'Item': 'Two'},
    'roomFive' : {'West': 'roomOne', 'North': 'roomSix', 'East': 'roomEight', 'Item': 'Four'},
    'roomSix' : {'South': 'roomFive', 'East': 'roomSeven', 'Item': 'Five'},
    'roomSeven': {'West': 'roomSix', 'Item': 'Six'},
    'roomFour': {'West': 'roomThree', 'Item': 'Three'},
    'roomEight': {'West': 'roomFive', 'Boss': 'Boss'}
}

COLORS = {
    # ... other colors ...
    'arrow_button_fg': '#1E90FF',  # Dodger Blue for arrow buttons
    'dialog_button_fg': '#4169E1',  # Royal Blue for default dialog buttons
    'collect_button_fg': '#228B22',  # Forest Green for collect item button
    'try_later_button_fg': '#DC143C',  # Crimson for try later button
    'frame_bg': '#F0F0F0',
    'button_bg': '#4CAF50',
    'button_hover': '#45a049',
    'button_text': '#FFFFFF',
    'try_later_button_bg': '#f44336',
    'try_later_button_hover': '#d32f2f',
    'dialog_bg': '#FFFFFF',
    'transparent': (255, 255, 255, 0),
    'connection': (200, 200, 200, 150),
    'room_fill': (220, 220, 220, 230),
    'room_border': (180, 180, 180, 255),
    'room_shadow': (0, 0, 0, 30),
    'room_highlight': (255, 255, 255, 50),
    'room_text': (0, 0, 0, 255),
    'explosion_bg': "black",
    'explosion_particles': ["red", "orange", "yellow"],
    'button_fg': '#4CAF50',  # Button foreground color
    'button_hover': '#45a049',  # Button hover color
}

SIZES = {
    'map_width': 400,
    'map_height': 400,
    'character_width': 20,
    'character_height': 20,
    'room_size': 85,
    'room_corner_radius': 20,
    'room_font_size': 12,
    'arrow_button_size': 40,
    'dialog_wraplength': 350,
    'explosion_width': 400,
    'explosion_height': 400,
    'explosion_particle_count': 100,
    'explosion_particle_speed': 5,
    'explosion_particle_min_radius': 2,
    'explosion_particle_max_radius': 5,
    'credits_width': 400,
    'credits_height': 400,
    'credits_wraplength': 350,
}
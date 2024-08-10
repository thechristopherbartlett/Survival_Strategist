import os
import tempfile
from src.modules.quotes import get_game_data, get_quote

# Existing configuration
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
QUOTES_PATH = "src/quotes.json" # TODO: Change in quotes.py currently hardcoded

# Get game data from quotes.py
ROOMS, ITEMS, ROOM_POSITION = get_game_data()

# Function to get quotes (can be used when needed)
GET_QUOTE = get_quote

# Existing color configurations
COLORS = {
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

# Existing size configurations
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
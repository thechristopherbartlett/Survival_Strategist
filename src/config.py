import os
import tempfile
import json
from src.modules.quotes import get_game_data, get_quote

# Existing configuration
START_ROOM = "roomOne"

# Add debug level option
#### CHANGE ME FOR RELEASE ####
DEBUG_LEVEL = "DEBUG"  # Can be "DEBUG", "INFO", "WARNING", "ERROR", or "CRITICAL"
FILE_DEBUG_LEVEL = "DEBUG"

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

# Load configuration from JSON file
with open('src/config.json', 'r') as config_file:
    config_data = json.load(config_file)

COLORS = config_data['COLORS']
SIZES = config_data['SIZES']

# Convert tuple values back to tuples
for key in ['transparent', 'connection', 'room_fill', 'room_border', 'room_shadow', 'room_highlight', 'room_text']:
    if key in COLORS:
        COLORS[key] = tuple(COLORS[key])
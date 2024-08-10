import json
import random
import logging
#from src.config import QUOTES_PATH
QUOTES_PATH = "src/config.json"

def load_quotes():
    """
    Module: load_quotes
    Date: 7/26/24
    Programmer: Timothy Stowe
    
    Purpose: Loads the quotes data from the JSON file.
    
    Version: 1.0
    RTM: 031
    """
    logging.debug("Loading quotes from file")
    try:
        with open(QUOTES_PATH, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error loading quotes file: {e}")
        return {}

def process_quotes(quotes):
    """
    Module: process_quotes
    Date: 7/26/24
    Programmer: Timothy Stowe
    
    Purpose: Processes the loaded quotes data into separate dictionaries for rooms, items, and room positions.
    
    Version: 1.0
    RTM: 032
    """
    logging.debug("Processing quotes data")
    rooms = {}
    items = {}
    room_positions = {}

    for room_name, room_data in quotes.items():
        if room_name.startswith('room'):
            rooms[room_name] = {
                'connections': room_data['connections'],
                'item': room_data.get('item')
            }
            room_positions[room_name] = tuple(room_data['position'])
            
            if 'item' in room_data:
                items[room_data['item']] = {
                    'room': room_name,
                    'key_message': room_data['key_message'],
                    'question': room_data.get('question'),
                    'answers': room_data.get('answers'),
                    'correct_answer': room_data.get('correct_answer')
                }
            elif 'boss' in room_data:
                items[room_data['boss']] = {
                    'room': room_name,
                    'key_message': room_data['key_message']
                }

    return rooms, items, room_positions

def get_game_data():
    """
    Module: get_game_data
    Date: 7/26/24
    Programmer: Timothy Stowe
    
    Purpose: Retrieves and processes the game data from the quotes file.
    
    Version: 1.0
    RTM: 033
    """
    logging.debug("Getting game data")
    quotes = load_quotes()
    return process_quotes(quotes)

def get_quote(item):
    """
    Module: get_quote
    Date: 7/26/24
    Programmer: Timothy Stowe
    
    Purpose: Retrieves a quote and associated data for a given item from the quotes file.
    If the item is not found, it returns a default message. This function also randomizes
    the order of answer options for multiple-choice questions.
    
    Version: 1.1
    RTM: 034
    """
    logging.debug(f"Getting quote for item: {item}")
    quotes = load_quotes()
    
    for room_name, room_data in quotes.items():
        if room_data.get('item') == item or room_data.get('boss') == item:
            quote_data = {
                "key_message": room_data['key_message'],
                "question": room_data.get('question', "No question available."),
                "answers": room_data.get('answers', []),
                "correct_answer": room_data.get('correct_answer', "")
            }
            
            # Randomize the order of the answers
            if quote_data["answers"]:
                quote_data["answers"] = random.sample(quote_data["answers"], len(quote_data["answers"]))
            
            logging.debug(f"Quote retrieved: {quote_data}")
            return quote_data
    
    logging.warning(f"No quote found for item: {item}")
    return {
        "key_message": "No quote found for this item.",
        "question": "No question available.",
        "answers": [],
        "correct_answer": ""
    }
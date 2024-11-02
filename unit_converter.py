"""
========================================
Universal Unit Converter 🚀📏💾
========================================

This script converts between different storage units (B, KB, MB, GB)
and distance units (mm, cm, m, km).
It's like a universal translator for your bytes and steps!

Author: Jose Luis Chafardet Grimaldi
Email: jose.chafardet@icloud.com
Created: Oct 19 2924
Last Modified: Oct 20 2023

May your storage always be sufficient and your distances accurately measured! 🎉
"""
from colorama import init, Fore, Style
import json  # Because who doesn't love a good JSON file? 📂
import logging  # Because every great app needs a diary! 📓
import argparse  # Because sometimes, you just want to talk to your app through the command line! 🖥️

# Initialize colorama
init()

# Set up logging to keep track of all the magic happening behind the scenes 🪄
logging.basicConfig(
    filename='unit_converter.log',  # Our app's personal diary 📔
    level=logging.INFO,  # We want to know all the juicy details (INFO and above)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Timestamped for posterity 🕒
)

# Log the start of the app
logging.info("Universal Unit Converter started. Ready to convert the world! 🌍")

# Hey there, unit conversion maestro! Ready to juggle some bytes and measure the universe? 🚀📏💾

# Load unit mappings from a JSON file
# This is where the magic happens - our units are now configurable! 🪄
def load_unit_mappings(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Oh no! The unit mappings file is missing. Did you forget to bring it to the party? 🎉")
        exit()
    except json.JSONDecodeError:
        print("Yikes! The unit mappings file is a bit of a mess. Did someone spill coffee on it? ☕")
        exit()

# Load the unit mappings from a JSON file
unit_mappings = load_unit_mappings('unit_mappings.json')

# Update the conversion functions to use the loaded mappings
def convert_storage(value, from_unit, to_unit):
    # Alright, let's set up our digital dance floor! 💃💾
    units = unit_mappings['storage']  # Now we're pulling from the JSON file - fancy, huh? 🎩

    # Debugging logs to trace the issue
    logging.debug(f"Converting {value} from {from_unit} to {to_unit}")
    logging.debug(f"From unit in bytes: {units[from_unit.upper()]}, To unit in bytes: {units[to_unit.upper()]}")

    # Final debugging attempt to trace the exact calculations
    logging.debug(f"Value: {value}, From Unit: {from_unit}, To Unit: {to_unit}")
    logging.debug(f"Bytes per {from_unit}: {units[from_unit.upper()]}, Bytes per {to_unit}: {units[to_unit.upper()]}")

    # Ensure the scaling factors are applied correctly
    bytes_value = value * units[from_unit.upper()]
    logging.debug(f"Intermediate bytes value: {bytes_value}")

    result = bytes_value / units[to_unit.upper()]
    logging.debug(f"Final result after conversion: {result}")

    return result

def convert_distance(value, from_unit, to_unit):
    # Time to stretch our legs and measure the world! 🌍🦵
    units = unit_mappings['distance']  # JSON-powered cosmic ruler! 🌌
    meters_value = value * units[from_unit.upper()]
    result = meters_value / units[to_unit.upper()]
    return result

def get_unit_input(prompt, valid_units):
    # Let's play a little Q&A game, shall we? 🎮
    while True:
        unit = input(prompt).upper()
        if unit in valid_units:
            return unit
        print(f"Oops! That unit is playing hide and seek. Try one of these: {', '.join(valid_units)}")

def get_numeric_input(prompt):
    # Let's make sure the user isn't trying to feed us alphabet soup! 🍲
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Oops! That doesn't look like a number. Try again, math wizard! 🧙‍♂️")

# Set up command-line argument parsing
# This is like giving our app ears to listen to your commands! 👂
def parse_arguments():
    parser = argparse.ArgumentParser(description="Universal Unit Converter - Convert storage and distance units like a pro! 🚀")
    parser.add_argument("conversion_type", choices=["storage", "distance"], help="Type of conversion: 'storage' for bytes, 'distance' for lengths")
    parser.add_argument("value", type=float, help="The value to convert. Go ahead, throw in a number!")
    parser.add_argument("from_unit", help="The unit you're converting from. Be specific!")
    parser.add_argument("to_unit", help="The unit you're converting to. Dream big!")
    return parser.parse_args()

# Check if the script is being run interactively or via command-line arguments
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        # Command-line mode
        args = parse_arguments()
        conversion_type = args.conversion_type
        value = args.value
        from_unit = args.from_unit.upper()
        to_unit = args.to_unit.upper()

        if conversion_type == 'storage':
            valid_units = list(unit_mappings['storage'].keys())
            convert_func = convert_storage
        elif conversion_type == 'distance':
            valid_units = list(unit_mappings['distance'].keys())
            convert_func = convert_distance

        if from_unit not in valid_units or to_unit not in valid_units:
            print(f"Oops! One of your units is not valid. Try one of these: {', '.join(valid_units)}")
            exit()

        # Perform the conversion
        result = convert_func(value, from_unit, to_unit)

        # Output the result
        print(f"Abracadabra! {value:,.2f} {from_unit} is equal to {Fore.GREEN}{result:,.2f}{Style.RESET_ALL} {Fore.YELLOW}{to_unit}{Style.RESET_ALL}")

        # Log the result
        logging.info(f"Command-line conversion: {value} {from_unit} to {to_unit} = {result}")
    else:
        # Interactive mode
        # Let's kick off this conversion party! 🎉

        # What's your flavor? Bytes or steps?
        print("What's your unit of choice today?")
        conversion_type = input("Type 'storage' for bytes and bits, or 'distance' for lengths and widths: ").lower()

        if conversion_type == 'storage':
            valid_units = list(unit_mappings['storage'].keys())
            convert_func = convert_storage
        elif conversion_type == 'distance':
            valid_units = list(unit_mappings['distance'].keys())
            convert_func = convert_distance
        else:
            print("Whoopsie! That's not on our menu. Let's call it a day, shall we?")
            exit()

        # Time for some number crunching!
        value = get_numeric_input("Enter the value (go wild!): ")

        # Where are we starting from?
        from_unit = get_unit_input(f"Enter the source unit ({', '.join(valid_units)}) - we don't judge: ", valid_units)

        # And where do we want to end up?
        to_unit = get_unit_input(f"Enter the target unit ({', '.join(valid_units)}) - the sky's the limit: ", valid_units)

        # Log the user's choices
        logging.info(f"Conversion type: {conversion_type}")
        logging.info(f"Value: {value}, From: {from_unit}, To: {to_unit}")

        # Time to work some magic! ✨🎩
        result = convert_func(value, from_unit, to_unit)

        # Log the result
        logging.info(f"Result: {result}")

        # Drum roll, please... 🥁
        print(f"Abracadabra! {value:,.2f} {from_unit} is equal to {Fore.GREEN}{result:,.2f}{Style.RESET_ALL} {Fore.YELLOW}{to_unit}{Style.RESET_ALL}")

        # Log the end of the app
        logging.info("Conversion completed. Another successful transformation! 🎉")

        # And there you have it, folks! You've just witnessed a unit transformation! 
        # Remember, whether it's bytes or meters, we're all just trying to measure up. 😉📏💻
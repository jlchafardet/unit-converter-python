"""
========================================
Universal Unit Converter 🚀📏💾
========================================

This script converts between different storage units (B, KB, MB, GB, TB, PB)
and distance units (mm, cm, m, km).
It's like a universal translator for your bytes and steps!

Author: Jose Luis Chafardet Grimaldi
Email: jose.chafardet@icloud.com
Created: Oct 19 2024
Last Modified: Oct 25 2024

May your storage always be sufficient and your distances accurately measured! 🎉
"""
from colorama import init, Fore, Style

# Initialize colorama
init()

# Hey there, unit conversion maestro! Ready to juggle some bytes and measure the universe? 🚀📏💾

def convert_storage(value, from_unit, to_unit):
    # Alright, let's set up our digital dance floor! 💃💾
    # Each unit gets a VIP pass with its value in bytes
    units = {
        'B': 1,                # Byte, the life of the party!
        'KB': 1024,            # Kilobyte, because 1024 is cooler than 1000
        'MB': 1024 ** 2,       # Megabyte, now we're talking!
        'GB': 1024 ** 3,       # Gigabyte, big player in the storage game
        'TB': 1024 ** 4,       # Terabyte, for when you have TOO MANY cat videos
        'PB': 1024 ** 5        # Petabyte, because sometimes, size really does matter
    }
    
    # First, let's convert our value to bytes. It's like converting everyone to a common language!
    bytes_value = value * units[from_unit.upper()]
    
    # Now, let's convert from bytes to our target unit. It's like translating back to our preferred dialect!
    result = bytes_value / units[to_unit.upper()]
    
    # Ta-da! Our converted value, ready to party in its new unit! 🎊
    return result

def convert_distance(value, from_unit, to_unit):
    # Time to stretch our legs and measure the world! 🌍🦵
    # Each unit gets a spot on our cosmic ruler
    units = {
        'MM': 0.001,    # Millimeter, for when you're feeling really small
        'CM': 0.01,     # Centimeter, perfect for measuring snails
        'M': 1,         # Meter, the OG of distance
        'KM': 1000      # Kilometer, for when you're going the extra mile (literally)
    }
    
    # First, let's convert to meters. It's like finding our common ground!
    meters_value = value * units[from_unit.upper()]
    
    # Now, let's convert from meters to our target unit. Stretch or shrink as needed!
    result = meters_value / units[to_unit.upper()]
    
    # Voila! Our distance, ready for its debut in its new unit! 🎭
    return result

def get_unit_input(prompt, valid_units):
    # Let's play a little Q&A game, shall we? 🎮
    while True:
        unit = input(prompt).upper()
        if unit in valid_units:
            return unit
        print(f"Oops! That unit is playing hide and seek. Try one of these: {', '.join(valid_units)}")

def get_float_input(prompt):
    # Let's get a number! No funny business, please! 🎲
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Whoa there! Negative numbers aren't invited to this party. Try again!")
                continue
            return value
        except ValueError:
            print("Oops! That doesn't look like a valid number. Give it another shot! 🎯")
        except KeyboardInterrupt:
            print("\nLooks like you decided to leave the party early. Catch you later! 👋")
            exit()

# Let's kick off this conversion party! 🎉

try:
    # What's your flavor? Bytes or steps?
    print("What's your unit of choice today?")
    conversion_type = input("Type 'storage' for bytes and bits, or 'distance' for lengths and widths: ").lower()

    if conversion_type == 'storage':
        valid_units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        convert_func = convert_storage
    elif conversion_type == 'distance':
        valid_units = ['MM', 'CM', 'M', 'KM']
        convert_func = convert_distance
    else:
        print("Whoopsie! That's not on our menu. Let's call it a day, shall we?")
        exit()

    # Time for some number crunching!
    value = get_float_input("Enter the value (go wild!): ")

    # Where are we starting from?
    from_unit = get_unit_input(f"Enter the source unit ({', '.join(valid_units)}) - we don't judge: ", valid_units)

    # And where do we want to end up?
    to_unit = get_unit_input(f"Enter the target unit ({', '.join(valid_units)}) - the sky's the limit: ", valid_units)

    # Time to work some magic! ✨🎩
    result = convert_func(value, from_unit, to_unit)

    # Drum roll, please... 🥁
    print(f"Abracadabra! {value:,.2f} {from_unit} is equal to {Fore.GREEN}{result:,.2f}{Style.RESET_ALL} {Fore.YELLOW}{to_unit}{Style.RESET_ALL}")

    # And there you have it, folks! You've just witnessed a unit transformation! 
    # Remember, whether it's bytes or meters, we're all just trying to measure up. 😉📏💻
except KeyboardInterrupt:
    print("\nLooks like you decided to leave the party early. Catch you later! 👋")
    exit()
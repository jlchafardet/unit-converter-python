"""
========================================
Universal Unit Converter 🚀📏💾
========================================

This script converts between different storage units (B, KB, MB, GB, TB, PB)
and distance units (mm, cm, m, km, inches).
It's like a universal translator for your bytes and steps!

Author: Jose Luis Chafardet Grimaldi
Email: jose.chafardet@icloud.com
Created: Oct 19 2024
Last Modified: ONov 2 2024

May your storage always be sufficient and your distances accurately measured! 🎉
"""
from colorama import init, Fore, Style

# Initialize colorama
init()

def show_help():
    # Time to spill the beans on all our secret sauce! 📚✨
    help_text = f"""
    {Fore.CYAN}🌟 Welcome to the Unit Converter Help Center! 🌟{Style.RESET_ALL}
    
    {Fore.YELLOW}Available Units:{Style.RESET_ALL}
    
    📦 Storage Units (because size matters!)
    • B  - Bytes (The tiny dancers of data)
    • KB - Kilobytes (A thousand-ish bytes having a party)
    • MB - Megabytes (Now we're talking serious business)
    • GB - Gigabytes (Perfect for your cat video collection)
    • TB - Terabytes (When you're a digital hoarder)
    • PB - Petabytes (You might need an intervention...)
    
    📏 Distance Units (for measuring your journey to the fridge)
    • MM - Millimeters (Tiny but mighty!)
    • CM - Centimeters (The Goldilocks of small measurements)
    • M  - Meters (The OG of measuring things)
    • KM - Kilometers (For when you're going places)
    • IN - Inches (Because sometimes you need to speak American)
    
    {Fore.GREEN}Pro Tips & Tricks:{Style.RESET_ALL}
    • Type 'help' at any prompt to see this guide
    • Numbers can include decimals (we don't judge!)
    • No negative numbers (we're positive people here)
    • Press Ctrl+C to exit (but we'll miss you!)
    
    {Fore.MAGENTA}Remember:{Style.RESET_ALL} Whether you're measuring digital space or physical place,
    we're here to make your conversion dreams come true! ✨
    """
    print(help_text)

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
        'KM': 1000,     # Kilometer, for when you're going the extra mile (literally)
        'IN': 0.0254    # Inch, because sometimes you just need a little bit more precision!
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
        unit = input(prompt).lower()
        if unit == 'help':
            show_help()
            continue
        if unit.upper() in valid_units:
            return unit.upper()
        print(f"Oops! That unit is playing hide and seek. Try one of these: {', '.join(valid_units)}")

def get_float_input(prompt):
    # Let's get a number! No funny business, please! 🎲
    while True:
        value = input(prompt).lower()
        if value == 'help':
            show_help()
            continue
        try:
            value = float(value)
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
    while True:  # Main program loop
        # What's your flavor? Bytes or steps?
        print(f"{Fore.CYAN}Welcome to the Unit Converter! Type 'help' at any time to see available options.{Style.RESET_ALL}")
        print("What's your unit of choice today?")
        conversion_type = input("Type 'storage' for bytes and bits, or 'distance' for lengths and widths: ").lower()

        if conversion_type == 'help':
            show_help()
            continue
        elif conversion_type == 'storage':
            valid_units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
            convert_func = convert_storage
        elif conversion_type == 'distance':
            valid_units = ['MM', 'CM', 'M', 'KM', 'IN']  # Fixed here
            convert_func = convert_distance
        else:
            print("Whoopsie! That's not on our menu. Let's try again!")
            continue

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

        # Ask if user wants to do another conversion
        again = input("\nWould you like to do another conversion? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for converting with us! See you next time! 👋")
            break

except KeyboardInterrupt:
    print("\nLooks like you decided to leave the party early. Catch you later! 👋")
    exit()
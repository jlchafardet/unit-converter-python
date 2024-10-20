"""
========================================
Storage Unit Converter 🚀💾
========================================

This script converts between different storage units (B, KB, MB, GB, TB, PB).
It's like a universal translator for your bytes!

Author: Jose Luis Chafardet Grimaldi
Email: jose.chafardet@icloud.com
Created: Oct 19 2924
Last Modified: Oct 19 2924

May your storage always be sufficient and your conversions accurate! 🎉
"""

# Hey there, storage unit converter extraordinaire! Let's break down some bytes, shall we? 🚀💾

def convert_storage(value, from_unit, to_unit):
    # Alright, let's set up our unit party! 🎉
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

# Let's take this baby for a spin, shall we? 🚗💨

# Ask the user for a value. Any value. Don't be shy!
value = float(input("Enter the value (go wild!): "))

# What unit are we starting with? B, KB, MB? The choice is yours!
from_unit = input("Enter the source unit (B, KB, MB, GB, TB, PB) - we don't judge: ")

# And where do we want to end up? Dream big!
to_unit = input("Enter the target unit (B, KB, MB, GB, TB, PB) - the sky's the limit: ")

# Time to work some magic! ✨🎩
result = convert_storage(value, from_unit, to_unit)

# Drum roll, please... 🥁
print(f"Abracadabra! {value} {from_unit} is equal to {result} {to_unit}")

# And there you have it, folks! You've just witnessed a storage unit transformation! 
# Remember, in the world of bytes, we're all just trying to find our place. 😉💻
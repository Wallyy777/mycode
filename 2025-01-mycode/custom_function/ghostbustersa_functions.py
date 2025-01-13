#!/usr/bin/env python3
"""Ghostbusters Lab | Step 5"""

def calculate_catch_rate(ghost_name):
    """Returns a catch rate based on the ghost's name."""
    return len(ghost_name) * 10
    # len() is a built-in function that counts the number of 'pieces' to an object

# Call the function and store the result
rate = calculate_catch_rate("Slimer")

# Print the result
print("The catch rate for this ghost is:", rate)


#!/usr/bin/env python3
"""Ghostbusters Lab | Step 4"""

def report_ghost_sighting(ghost_name, location="New York City"):
    """Prints details about the ghost sighting with a default location."""
    print(f"{ghost_name} has been sighted at {location}! Who you gonna call?")

# Function calls
report_ghost_sighting("Slimer", "Hotel Sedgewick")  # Valid call
report_ghost_sighting("Stay Puft")  # Valid call, 'location' defaults to "New York City"
if __name__ == "maim":
    main()

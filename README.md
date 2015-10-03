# space-allocation
This exercise models a space allocation system for staffs and fellows

# Run Test
To run test run python test_main.py

# Running the script
from main import ReadFromTextFile
result = ReadFromTextFile().read_then_allocate()
result = ReadFromTextFile()

# To Get a list of allocations
result.read_then_allocate()

# Get list of available rooms
result.office.list_of_available_rooms()

# Get list of unavaialable rooms
result.office.list_of_filled_rooms()

# Get the no of occupant in a room given the office name
result.office.no_of_occupant_in_the_room(office_name")

# Add an offfice
result.office.add_staff_office(office_name)

# Remove office
result.office.remove_staff_office(office_name)

# Rename office
result.office.rename_office_name(old_name, new_office)
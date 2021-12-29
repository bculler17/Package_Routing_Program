import csv
from HashTable import HashTable

# Read package data from the provided csv file:
with open('./WGUPS_data/package_data.csv', 'r') as csv_file:
    # Create a csv reader object:
    read_csv = csv.reader(csv_file, delimiter=',')

    # Initialize list that represents all of the packages needing to be delivered
    packages = []
    # Initialize list that represents the first truck route and payload
    first_truck = []
    # Initialize list that represents the second truck route and payload
    second_truck = []
    # list that represents the final truck route and payload
    first_truck_second_trip = []

    # Extract each data row (i.e. each package) one by one
    # Space-time complexity is O(N)
    for row in read_csv:
        package_id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        delivery_deadline = row[5]
        mass_kg = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'

        package_item = [package_id, address_location, address, city, state, zipcode, delivery_deadline, mass_kg, note,
                        delivery_start, delivery_status]

        packages.append(package_item)

        # Load the packages onto the trucks according to their constraints:
        if delivery_deadline != 'EOD':
            if 'Must' in note or 'None' in note:           # 'Must' = this package MUST travel with a specific package
                first_truck.append(package_item)                      # this is a list that represents the first truck
        if 'Can only be' in note:                                     # note = "Can only be on truck 2"
            second_truck.append(package_item)                         # this is a list that represents the second truck
        if 'Delayed' in note:
            second_truck.append(package_item)
        if '84104' in zipcode and '10:30' not in delivery_deadline:
            first_truck_second_trip.append(package_item)
        # change the wrong address package to the correct address
        if 'Wrong address listed' in note:
            address = '410 S State St'
            zipcode = '84111'
            first_truck_second_trip.append(package_item)
        if package_item not in first_truck and package_item not in second_truck and package_item not in \
                first_truck_second_trip:
            if len(second_truck) > len(first_truck_second_trip):
                first_truck_second_trip.append(package_item)
            else:
                second_truck.append(package_item)

    hash_table = HashTable()  # Initialize a hash table object

    # Space-time complexity is O(N)
    for p in packages:
        # Insert package into hash table
        hash_table.add(p[0], p)

    # Get the payload of the first truck
    # Space-time complexity is O(1)
    def get_first_truck_payload():
        return first_truck

    # Get the payload of the second truck
    # Space-time complexity is O(1)
    def get_second_truck_payload():
        return second_truck

    # Get the payload of the third truck (second trip of the 1st truck)
    # Space-time complexity is O(1)
    def get_first_truck2_payload():
        return first_truck_second_trip

    # Get full list of packages
    # Space-time complexity is O(1)
    def get_hash_table():
        return hash_table
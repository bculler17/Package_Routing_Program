import WGUPS_data.csv_distance_calculator
import WGUPS_data.csv_pkg_loader

# initialize route and distance lists
first_route = []
second_route = []
third_route = []

# The times that the trucks leave the HUB
first_start_time = ['8:00:00']
second_start_time = ['9:10:00']      # leaves as soon as the delayed packages arrive at the HUB at 9:05
third_start_time = ['11:00:00']      # leaves when the first truck returns and after a wrong address is corrected

# The payloads from each route
first_payload = WGUPS_data.csv_pkg_loader.get_first_truck_payload()
second_payload = WGUPS_data.csv_pkg_loader.get_second_truck_payload()
third_payload = WGUPS_data.csv_pkg_loader.get_first_truck2_payload()

# Consolidate into one list to iterate through
route_list = [first_route, second_route, third_route]
start_time_list = [first_start_time, second_start_time, third_start_time]
payload_list = [first_payload, second_payload, third_payload]

# Update the delivery start time of all packages in each truck to when each respective truck leaves the HUB
# Space-time complexity is O(N^2)
i = 0    # counter to iterate through the route_list and start_time_list
for payload in payload_list:
    for index, package in enumerate(payload):
        payload[index][9] = start_time_list[i][0]
        route_list[i].append(payload[index])
    i += 1

# Compare route addresses to address list in address_data.csv
# and set the "address_location" of each package = address index from address list in address_data.csv
# Space-time complexity is O(N^3)
for route in route_list:
    for index, outer in enumerate(route):
        for inner in WGUPS_data.csv_distance_calculator.get_address_list():
            if outer[2] == inner[2]:                    # if route address = address from address list
                route[index][1] = inner[0]              # set the "address_location" of each package = address index

# Call algorithm to sort packages for each route
# Third parameter '0' = the HUB : Starting point is from the hub
# Third parameter '24' = the delayed package (Package 25) address location
# Space-time complexity is O(1)
WGUPS_data.csv_distance_calculator.get_optimal_route(first_route, 1, 0)
WGUPS_data.csv_distance_calculator.get_optimal_route(second_route, 2, 24)  # Start here to meet Delivery Deadline
WGUPS_data.csv_distance_calculator.get_optimal_route(third_route, 3, 0)

# Calculate the total distance traveled by truck 1 and the distance of each package
total_distance1 = 0

# Add the distances from the other delivery locations
# Space-time complexity is O(N)
for index in range(len(WGUPS_data.csv_distance_calculator.get_first_route_indexes())):
    try:
        # Get the total distance traveled
        total_distance1 = WGUPS_data.csv_distance_calculator.\
            get_distance(int(WGUPS_data.csv_distance_calculator.get_first_route_indexes()[index]),
                         int(WGUPS_data.csv_distance_calculator.get_first_route_indexes()[index + 1]),
                         total_distance1)
        # Get the time of delivery
        deliver_package = WGUPS_data.csv_distance_calculator.\
            get_total_time(WGUPS_data.csv_distance_calculator.
                           get_current_distance(int(WGUPS_data.csv_distance_calculator.
                                                    get_first_route_indexes()[index]),
                                                int(WGUPS_data.csv_distance_calculator.
                                                    get_first_route_indexes()[index + 1])), first_start_time)
        # Update all of the packages with the delivery date
        WGUPS_data.csv_distance_calculator.get_first_route_addresses()[index][10] = (str(deliver_package))
        # Update the hash table with the updated packages
        WGUPS_data.csv_pkg_loader.get_hash_table().update(
            int(WGUPS_data.csv_distance_calculator.get_first_route_addresses()[index][0]), first_route[index])
    except IndexError:
        pass

# Calculate the total distance traveled by truck 2 and the distance of each package
total_distance2 = 0

# Add the distances from the other delivery locations
# Space-time complexity is O(N)
for index in range(len(WGUPS_data.csv_distance_calculator.get_second_route_indexes())):
    try:
        # Get the total distance traveled
        total_distance2 = WGUPS_data.csv_distance_calculator.\
            get_distance(int(WGUPS_data.csv_distance_calculator.get_second_route_indexes()[index]),
                         int(WGUPS_data.csv_distance_calculator.get_second_route_indexes()[index + 1]),
                         total_distance2)
        # Get the time of delivery
        deliver_package2 = WGUPS_data.csv_distance_calculator.\
            get_total_time(WGUPS_data.csv_distance_calculator.
                           get_current_distance(int(WGUPS_data.csv_distance_calculator.
                                                    get_second_route_indexes()[index]),
                                                int(WGUPS_data.csv_distance_calculator.
                                                    get_second_route_indexes()[index + 1])), second_start_time)
        # Update all of the packages with the delivery date
        WGUPS_data.csv_distance_calculator.get_second_route_addresses()[index][10] = (str(deliver_package2))
        # Update the hash table with the updated packages
        WGUPS_data.csv_pkg_loader.get_hash_table().update(
            int(WGUPS_data.csv_distance_calculator.get_second_route_addresses()[index][0]), second_route[index])
    except IndexError:
        pass

# Calculate the total distance traveled by truck 3 and the distance of each package
total_distance3 = 0

# Add the distances from the other delivery locations
# Space-time complexity is O(N)
for index in range(len(WGUPS_data.csv_distance_calculator.get_third_route_indexes())):
    try:
        # Get the total distance traveled
        total_distance3 = WGUPS_data.csv_distance_calculator.\
            get_distance(int(WGUPS_data.csv_distance_calculator.get_third_route_indexes()[index]),
                         int(WGUPS_data.csv_distance_calculator.get_third_route_indexes()[index + 1]),
                         total_distance3)
        # Get the time of delivery
        deliver_package3 = WGUPS_data.csv_distance_calculator.\
            get_total_time(WGUPS_data.csv_distance_calculator.
                           get_current_distance(int(WGUPS_data.csv_distance_calculator.
                                                    get_third_route_indexes()[index]),
                                                int(WGUPS_data.csv_distance_calculator.
                                                    get_third_route_indexes()[index + 1])), third_start_time)
        # Update all of the packages with the delivery date
        WGUPS_data.csv_distance_calculator.get_third_route_addresses()[index][10] = (str(deliver_package3))
        # Update the hash table with the sorted packages
        WGUPS_data.csv_pkg_loader.get_hash_table().update(
            int(WGUPS_data.csv_distance_calculator.get_third_route_addresses()[index][0]), third_route[index])
    except IndexError:
        pass


# Get the total mileage traveled by all trucks
# Space-time complexity is O(1)
def total_distance():
    # Bring the trucks back to the HUB:
    last_index1 = len(WGUPS_data.csv_distance_calculator.get_first_route_indexes()) - 1
    tot_distance1 = WGUPS_data.csv_distance_calculator.get_distance(
        int(WGUPS_data.csv_distance_calculator.get_first_route_indexes()[last_index1][1]), 0, total_distance1)
    last_index2 = len(WGUPS_data.csv_distance_calculator.get_second_route_indexes()) - 1
    tot_distance2 = WGUPS_data.csv_distance_calculator.get_distance(
        int(WGUPS_data.csv_distance_calculator.get_second_route_indexes()[last_index2][1]), 0, total_distance2)
    last_index3 = len(WGUPS_data.csv_distance_calculator.get_third_route_indexes()) - 1
    tot_distance3 = WGUPS_data.csv_distance_calculator.get_distance(
        int(WGUPS_data.csv_distance_calculator.get_third_route_indexes()[last_index3][1]), 0, total_distance3)
    return tot_distance1 + tot_distance2 + tot_distance3

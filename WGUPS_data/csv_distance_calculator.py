import csv
import datetime

# Read distance data from the provided csv file:
with open('./WGUPS_data/distance_data.csv', 'r') as csvfile_1:
    distance_csv = list(csv.reader(csvfile_1, delimiter=','))
# Read distance name data from the provided csv file:
with open('./WGUPS_data/address_data.csv', 'r') as csvfile_2:
    distance_name_csv = list(csv.reader(csvfile_2, delimiter=','))

    # Get the complete list of addresses that packages are to be delivered to
    # Space-time complexity is O(1)
    def get_address_list():
        return distance_name_csv

    # Calculate the total distance traveled on the route after traveling from address1 (row) to address2 (col)
    # Space-time complexity is O(1)
    def get_distance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return total + float(distance)

    # Calculate the distance between address1 (row) and address2 (col)
    # Space-time complexity is O(1)
    def get_current_distance(row, col):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return float(distance)

    # Calculate the total time traveled for a given truck/package to determine delivery time of a package
    # (The delivery and loading times of packages are factored into the calculation of the average speed of the trucks)
    # Space-time complexity is O(N)
    def get_total_time(distance, truck_time_list=[]):
        time_in_hours = distance / 18       # Trucks travel at an average speed of 18 miles per hour
        time_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(time_in_hours * 60, 60))
        final_time = time_in_minutes + ':00'
        truck_time_list.append(final_time)
        total_time = datetime.timedelta()
        for time in truck_time_list:
            (h, m, s) = time.split(':')
            t = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            total_time += t
        return total_time

    # Initialize the truck routes
    first_route_addresses = []
    first_route_indexes = []
    second_route_addresses = []
    second_route_indexes = []
    third_route_addresses = []
    third_route_indexes = []

    # Implement the following recursive greedy algorithm to determine a potential optimal truck route
    # Fist parameter = list of addresses to be sorted
    # Second parameter = the truck number: 1, 2, or 3
    # Third parameter = the current location of the truck, identified by the address index from address_data.csv
    # First and third parameters are updated after each iteration
    # Space-time complexity is O(N^2)
    def get_optimal_route(address_list, truck_num, current_location):
        # Break the recursion once all of the addresses have been sorted
        if len(address_list) == 0:
            return address_list
        else:
            try:
                lowest_value = 50.0
                new_location = 0
                for address in address_list:
                    # address[1] is the address_location (the address index from address_data.csv)
                    if get_current_distance(current_location, int(address[1])) <= lowest_value:
                        lowest_value = get_current_distance(current_location, int(address[1]))
                        new_location = int(address[1])
                for address in address_list:
                    if get_current_distance(current_location, int(address[1])) == lowest_value:
                        if truck_num == 1:
                            first_route_addresses.append(address)
                            first_route_indexes.append(address[1])
                            pop_address = address_list.index(address)
                            address_list.pop(pop_address)
                            current_location = new_location
                            get_optimal_route(address_list, 1, current_location)
                        elif truck_num == 2:
                            second_route_addresses.append(address)
                            second_route_indexes.append(address[1])
                            pop_address = address_list.index(address)
                            address_list.pop(pop_address)
                            current_location = new_location
                            get_optimal_route(address_list, 2, current_location)
                        elif truck_num == 3:
                            third_route_addresses.append(address)
                            third_route_indexes.append(address[1])
                            pop_address = address_list.index(address)
                            address_list.pop(pop_address)
                            current_location = new_location
                            get_optimal_route(address_list, 3, current_location)
            except IndexError:
                pass

    first_route_indexes.insert(0, '0')

    # Space-time complexity is O(1)
    def get_first_route_indexes():
        return first_route_indexes

    # Space-time complexity is O(1)
    def get_first_route_addresses():
        return first_route_addresses

    second_route_indexes.insert(0, '0')

    # Space-time complexity is O(1)
    def get_second_route_indexes():
        return second_route_indexes

    # Space-time complexity is O(1)
    def get_second_route_addresses() -> object:
        """

        :rtype: object
        """
        return second_route_addresses

    third_route_indexes.insert(0, '0')

    # Space-time complexity is O(1)
    def get_third_route_indexes():
        return third_route_indexes

    # Space-time complexity is O(1)
    def get_third_route_addresses():
        return third_route_addresses






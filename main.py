# Beth Culler Student ID#: 001003662

import datetime
import WGUPS_data.csv_pkg_loader
import routing


class Main:
    # The welcome display when the program is started
    global convert_start_time, hashtable, delivery_start, convert_delivery_time, delivery_end
    print('-------------------------------------------')
    print('WGUPS -')
    print('Routing and Delivery Distribution Program')
    print('-------------------------------------------\n')
    print(f'Total mileage traveled by all trucks: {routing.total_distance():.2f} miles.')
    start = input("What would you like to do? \n"
                  "Please choose a number\n"
                  "1: Search for the status and info of a specific package \n"
                  "2: Search for the status and info of all packages \n"
                  "3: View Route Info \n"
                  "4: Exit the program")
    # Space-time complexity is O(N)
    while start != 'exit':
        if start == '1':
            # User is interested in searching for only one particular package
            try:
                id = int(input('Please enter the ID of the package you would like to view: \n'
                               'PackageID = '))
                hashtable = WGUPS_data.csv_pkg_loader.get_hash_table()
                delivery_start = hashtable.get(id)[9]
                delivery_end = hashtable.get(id)[10]
                time_of_interest = input('What time would you like to check the status of PackageID ' + str(id) +
                                         '? \n Time (HH24:MI:SS) = ')
                (h, m, s) = time_of_interest.split(':')
                convert_chosen_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = delivery_start.split(':')
                convert_start_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = delivery_end.split(':')
                convert_end_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                print('Status and Info of PackageID ' + str(id) + ' at ' + time_of_interest + ':')
                # Check to see whether the package has left the HUB yet
                if convert_start_time >= convert_chosen_time:
                    # The package has not left the HUB yet
                    hashtable.get(id)[10] = 'AT THE HUB'
                    hashtable.get(id)[9] = 'departs at ' + delivery_start
                    print('Package ID:', hashtable.get(id)[0], ' Street Address:',
                          hashtable.get(id)[2], hashtable.get(id)[3],
                          hashtable.get(id)[4], hashtable.get(id)[5],
                          ' Delivery Deadline:', hashtable.get(id)[6],
                          ' Package Weight KG:', hashtable.get(id)[7], ' Truck Status:',
                          hashtable.get(id)[9], ' Delivery Status:', hashtable.get(id)[10])
                elif convert_start_time <= convert_chosen_time:
                    # The package has left the HUB; check to see if it has been delivered yet
                    if convert_chosen_time < convert_end_time:
                        # The package is still in transit and has not been delivered yet
                        hashtable.get(id)[10] = 'EN ROUTE'
                        hashtable.get(id)[9] = 'departs at ' + delivery_start
                        print('Package ID:', hashtable.get(id)[0], ' Street Address:',
                              hashtable.get(id)[2], hashtable.get(id)[3],
                              hashtable.get(id)[4], hashtable.get(id)[5],
                              ' Delivery Deadline:', hashtable.get(id)[6],
                              ' Package Weight KG:', hashtable.get(id)[7], ' Truck Status:',
                              hashtable.get(id)[9], ' Delivery Status:', hashtable.get(id)[10])
                    else:
                        # The package has been delivered
                        hashtable.get(id)[10] = 'DELIVERED at ' + delivery_end
                        hashtable.get(id)[9] = 'departed at ' + delivery_start
                        print('Package ID:', hashtable.get(id)[0], ' Street Address:',
                              hashtable.get(id)[2], hashtable.get(id)[3],
                              hashtable.get(id)[4], hashtable.get(id)[5],
                              ' Delivery Deadline:', hashtable.get(id)[6],
                              ' Package Weight KG:', hashtable.get(id)[7], ' Truck Status:',
                              hashtable.get(id)[9], ' Delivery Status:', hashtable.get(id)[10])
                print('Thank you. Goodbye.')
                exit()
            except ValueError:
                print('Invalid entry. Please try again.')
                exit()
        elif start == '2':
            # User would like to view the status and info of every package at a specific time
            # Prompt user for which time they would like to search for
            try:
                pkg_status_time = input('Please enter the time you would like to view: \n'
                                        'Time (HH24:MI:SS) = ')
                (h, m, s) = pkg_status_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                print('Status and Info of all packages at ' + pkg_status_time + ':')
                for count in range(1, 41):
                    try:
                        hashtable = WGUPS_data.csv_pkg_loader.get_hash_table()
                        delivery_start = hashtable.get(count)[9]
                        delivery_end = hashtable.get(count)[10]
                        (h, m, s) = delivery_start.split(':')
                        convert_start_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = delivery_end.split(':')
                        convert_delivery_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass
                    # Check to see whether each package has left the HUB yet
                    if convert_start_time >= convert_user_time:
                        # The package has not left the HUB yet
                        hashtable.get(count)[10] = 'AT THE HUB'
                        hashtable.get(count)[9] = 'departs at ' + delivery_start
                        print('Package ID:', hashtable.get(count)[0], ' Street Address:',
                              hashtable.get(count)[2], hashtable.get(count)[3],
                              hashtable.get(count)[4], hashtable.get(count)[5],
                              ' Delivery Deadline:', hashtable.get(count)[6],
                              ' Package Weight KG:', hashtable.get(count)[7], ' Truck Status:',
                              hashtable.get(count)[9], ' Delivery Status:', hashtable.get(count)[10])
                    elif convert_start_time <= convert_user_time:
                        # The package has left the HUB; check to see if it has been delivered yet
                        if convert_user_time < convert_delivery_time:
                            # The package is still in transit and has not been delivered yet
                            hashtable.get(count)[10] = 'EN ROUTE'
                            hashtable.get(count)[9] = 'departed at ' + delivery_start
                            print('Package ID:', hashtable.get(count)[0], ' Street Address:',
                                  hashtable.get(count)[2], hashtable.get(count)[3],
                                  hashtable.get(count)[4], hashtable.get(count)[5],
                                  ' Delivery Deadline:', hashtable.get(count)[6],
                                  ' Package Weight KG:', hashtable.get(count)[7], ' Truck Status:',
                                  hashtable.get(count)[9], ' Delivery Status:', hashtable.get(count)[10])
                        else:
                            # The package has been delivered
                            hashtable.get(count)[10] = 'DELIVERED at ' + delivery_end
                            hashtable.get(count)[9] = 'departed at ' + delivery_start
                            print('Package ID:', hashtable.get(count)[0], ' Street Address:',
                                  hashtable.get(count)[2], hashtable.get(count)[3],
                                  hashtable.get(count)[4], hashtable.get(count)[5],
                                  ' Delivery Deadline:', hashtable.get(count)[6],
                                  ' Package Weight KG:', hashtable.get(count)[7], ' Truck Status:',
                                  hashtable.get(count)[9], ' Delivery Status:', hashtable.get(count)[10])
                print('Thank you. Goodbye.')
                exit()
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry. Please try again.')
                exit()
        elif start == '3':
            print('ROUTE 1 Deliveries:')
            print('Total Packages: ' + str(len(WGUPS_data.csv_pkg_loader.get_first_truck_payload())))
            print('Western Governors University HUB-> ')
            max = len(WGUPS_data.csv_distance_calculator.get_first_route_indexes()) - 2
            for i in range(0, max):
                print(WGUPS_data.csv_distance_calculator.get_first_route_addresses()[i][2] + ' -> ' +
                      WGUPS_data.csv_distance_calculator.get_first_route_addresses()[i + 1][2] + ' -> ')
            print('BACK TO HUB: Route 1 complete.')
            print('ROUTE 2 Deliveries:')
            print('Total Packages: ' + str(len(WGUPS_data.csv_pkg_loader.get_second_truck_payload())))
            print('Western Governors University HUB-> ')
            max = len(WGUPS_data.csv_distance_calculator.get_second_route_indexes()) - 2
            for i in range(0, max):
                print(WGUPS_data.csv_distance_calculator.get_second_route_addresses()[i][2] + ' -> ' +
                      WGUPS_data.csv_distance_calculator.get_second_route_addresses()[i + 1][2] + ' -> ')
            print('BACK TO HUB: Route 2 complete.')
            print('ROUTE 3 Deliveries:')
            print('Total Packages: ' + str(len(WGUPS_data.csv_pkg_loader.get_first_truck2_payload())))
            print('Western Governors University HUB-> ')
            max = len(WGUPS_data.csv_distance_calculator.get_third_route_indexes()) - 2
            for i in range(0, max):
                print(WGUPS_data.csv_distance_calculator.get_third_route_addresses()[i][2] + ' -> ' +
                      WGUPS_data.csv_distance_calculator.get_third_route_addresses()[i + 1][2] + ' -> ')
            print('BACK TO HUB: Route 3 complete.')
            print('Thank you. Goodbye.')
            exit()
        elif start == '4':
            # User chose to exit the program
            print('Thank you. Goodbye.')
            exit()
        else:
            print('Something unexpected happened. Goodbye.')
            exit()
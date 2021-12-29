class HashTable(object):
    # Constructor to create a hash table "from scratch" (i.e. without using additional libraries or classes).
    # Constraints per project requirements: unable to use dictionaries or any other data type that rely on hash tables.
    # This constructor therefore creates a hash table using an array.
    # Space-time complexity is O(1)
    def __init__(self, length=40) -> object:
        """

        :rtype: object
        """
        # Initialize the array with 40 empty values (i.e. zero packages).
        self.array = [None] * length

    # Get the index# of the array for a specific key (key = the package ID number)
    # Space-time complexity is O(1)
    def hash(self, key):
        length = len(self.array)
        return key % length

    # To avoid collisions and to therefore avoid more frequent linear lookups through list iterations,
    # and to instead ensure more frequent constant lookups -
    # create a self-adjusting hash table
    # by making the length of the array flexible.
    # Enable the ability to expand the array if the array becomes too populated
    # Space-time complexity is O(N)
    def is_full(self):
        # Determine if the array is too populated:
        items = 0
        # Count how many indexes exist in the array that contain packages:
        for item in self.array:
            if item is not None:
                items += 1
        full_bool = items > len(self.array) / 2
        # Return true if the amount of populated items is more than half the length of the list:
        return full_bool

    # Double the array length and re-add values
    # Space-time complexity is O(N^2)
    def double(self):
        dht = HashTable(length=len(self.array) * 2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue

            # Re-add all of the packages to the new array for its key to return the correct index:
            for pid in self.array[i]:
                dht.add(pid[0], pid[1])

        # Replace the original, smaller array with the new, larger array:
        self.array = dht.array

    # Add a package into the array (the hash table) by its key (key = the package ID number)
    # Space-time complexity is O(N)
    def add(self, key, value=[11]):
        """Add a value to our array by its key"""
        index = self.hash(key)
        if self.array[index] is not None:
            # This index already contains one or more packages.
            # This means that this insert MIGHT be an update to a package that already exists.
            # Determine if the package already exists at this location:
            for kvp in self.array[index]:
                # If package ID number is found, then update its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                # The package ID number does not already exist at this location.
                # Insert the package at the end of the list located at this index#.
                self.array[index].append([key, value])
        else:
            # This index is empty.
            # Initiate a list and insert the package at this location.
            self.array[index] = []
            self.array[index].append([key, value])
        # To help avoid collisions -
        # If the array is more than half full, double the size of the array before inserting the new package:
        if self.is_full():
            self.double()

    # Update package in hash table
    # Space-time complexity is O(N)
    def update(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for pair in self.array[index]:
                if pair[0] == key:
                    pair[1] = value
        else:
            print('This key does not yet exist in the hash table: Update not possible. \n'
                  'Please add key:value pair to hash table instead of trying to execute an update.')

    # Get package details by its key (key = the package ID number)
    # Space-time complexity is O(N)
    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs to determine if the package exists.
            # If the package exists, return its value.
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]

            # If no return was done during loop,
            # it means the package doesn't exist.
            raise KeyError()
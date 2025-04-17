# This file contains my observations and notes about Hash Table
# I have also created my own Hash Table Class to understand the DS

# Observations
# Dictionaries act like built-in hash tables. They are made up of a key|value pair
# {"Nails": 1000} --> {"key":value}
# The way the hash table works is that there is a hash function(method). What we're going to do is perform a hash on the key,
# by running the key through the hash, and in addition to returning a key|value pair we also get an address.
# The address is the location of where we store the key|value pair
# There are two important charatistics about a hash:
# 1. This is a one-way relationship.
    # We cannot take the address and produce nails.
# 2. It is deterministic; everytime we put in the key "nails" we will always expect to get the number 2.
# Python does have it's own built-in hash, but for the sake of learning, I will be making my own from scratch
# So I will be using a list as an address space. Which means, when I put in pairs into my address space,
# I will be creating lists within a list.

# When inputting pairs into an address space, sometimes there can be a collision. A collision happens
# when you put a key|value pair at an address already occupied by another key|value pair.
# In order to allow for more than one pair existing within one address space, we are going to make a list of lists at an address space.
# For example: At an address space of 2 there is a list of lists: [["Nails": 1000], ["Nails": 1000]] This is also known as seperate chaining.
# There is also another popular way with dealing with collisions, is to iterate through the address space until there is an unoccupied space.
# This method is also known as Linear Probing (a form of open addressing).
# There is also another method to do seperate chaining, where you can have a linked list at each address space. 

# An important point about hash tables is that you should always have a prime number of addresses. The reason being, the addition of a prime 
# number of spaces increases the amount of randomness for how the key|value pairs are going to be distrubted through the hash table. Thus,
# reducing your # of collisions.

class HashTable:
    # the default parameter is set to 7
    def __init__(self, size = 7):
        # creates a list with 7 items which all contain None
        self.data_map = [None] * size
    
    # the main hash method
    def __hash(self, key):
        # init to 0
        my_hash = 0
        # for each letter in the key we will run this calculation
        for letter in key:
            # ord() --> ordinal which retrieves the ASCII numerical value for each letter 
            # we multiply by 23 (or any prime number)
            # we utilize the modulo operator by dividing by the length of the data_map and calculate the remainder
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        # return the hash_table
        return my_hash

    # print function
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        # retrieving the address space
        index = self.__hash(key)
        # now we have to init the empty list at that address
        # we only want to do this, if this space is not occupied a.k.a the list has not been created yet
        if self.data_map[index] is None:
            self.data_map[index] = []
        # adding the key value pair as a list by appending it to the list
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        # retrieve the address space by using the hash function
        index = self.__hash(key)
        # we only want to look for items in a specific address space if there are items within that address space
        if self.data_map[index] is not None:
            # since there are items within this address space we want to loop through them
            # specifically, we are looping through the list within the address space
            for i in range(len(self.data_map[index])):
                # this might look complex but what we are doing is grabbing the i (index) of the pair within the list at that specific address 
                # space. From there we are grabbing the key --> [0] and determining if that is equal to the given key
                if self.data_map[index][i][0] == key:
                    # we make sure to select [1] since that is the index of the value
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        # creating a list where we will place our keys
        all_keys = []
        # for loop to iterate through entire address space
        for i in range(len(self.data_map)):
            # if a specific index has occupied data than we run a for loop
            if self.data_map[i] is not None:
                # for loop to iterate through lists within a single address space
                for j in range(len(self.data_map[i])):
                    # now we just need to append the keys data into all_keys
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
            
my_hash_table = HashTable()

print("Printing Hash Table after using the constructor function:")
my_hash_table.print_table()

print("")
print("Testing out set_item function by inserting: [Pokemon, 1000], and [Clash of Clans, 500]")
my_hash_table.set_item("Pokemon", 1000)
my_hash_table.set_item("Clash of Clans", 500)
my_hash_table.print_table()

print("")
print("Testing out get_item function by returning the value of key Pokemon:")
print(my_hash_table.get_item("Pokemon"))

print("")
print("Testing out get_item function by returning the value of a fake key Pokemons:")
print(my_hash_table.get_item("Pokemons"))

print("")
print("Testing out keys function:")
print(my_hash_table.keys())
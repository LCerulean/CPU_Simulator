#Bus sends control signals and data between processor and other components
#Needs to help CPU communicate with memory (cashe)


bus_max_size = 128

class Memory:
    def __init__(self):
        # Bus dict pairs = address:value
        self.memory_bus = {}
        self.create_bus()

    # Used in __init__, builds address location (binary) in memory bus and sets value to 0
    def create_bus(self):
        for i in range(bus_max_size):
            self.memory_bus['{0:08b}'.format(i)] = 0

    # Returns value of inputted address if it exists
    def search_bus(self, address):
        if self.memory_bus.get(address) is not None:
            return self.memory_bus.get(address)
        return None

    # If the address:value does not exist in the memory bus, adds it to memory_bus dict
    def add_to_bus(self, address, value):
        if self.memory_bus.get(address) is not None:
            self.memory_bus[address] = value
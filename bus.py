#Bus sends control signals and data between processor and other components
#In actual CPU is needed to help CPU communicate with memory

bus_max_size = 64

class Bus:
    def __init__(self):
        # Bus dict pairs = address:value
        self.memory_bus = {}
        self.create_bus()

    # Used in __init__, builds address location (in binary) in memory bus and sets value to 0
    def create_bus(self):
        for i in range(bus_max_size):
            self.memory_bus[f'{i:08b}'] = 0

    # Returns value of input address if it exists
    def search_bus(self, address):
        if self.memory_bus.get(address) is not None:
            return self.memory_bus.get(address)
        return None

    # If the address is in the memory_bus, updates current value in memory_bus dict to input value
    def add_to_bus(self, address, value):
        if self.memory_bus.get(address) is not None:
            self.memory_bus[address] = value
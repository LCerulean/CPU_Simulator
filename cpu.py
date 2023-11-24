# CPU instruction cycle stages:
    # 1: fetch
    # 2: decode
    # 3: execute
    # 4: memory access
    # 5: registry write-back

from cache import Cache
from bus import Bus

class CPU:
    def __init__(self):
        self.cache = Cache()
        self.bus = Bus()
        self.registers = [0] * 8
        self.counter = 0


    # Step 1: Retrieves file ("memory") information
    def fetch_file_contents(self, file):
        print(f"Fetching file: {file}\n")
        open_file = open(file, 'r')
        file_contents = open_file.readlines()
        for i in file_contents:
            file_contents[file_contents.index(i)] = i.strip()
        return file_contents


    # Step 2: Instructions are deciphered and each one is carried out as it is decoded.
    def decode_file_contents(self, file_contents, data_or_instruction):
        if data_or_instruction == 'data':
            print(f"File contains data, decoding data...\n")
            for content in file_contents:
                print(f"Decoded: {content}\n")
                content_piece = content.split(',')
                self.access_memory(content_piece[0], content_piece[1])
                print()
        elif data_or_instruction == 'instruction':
            print(f"File contains instructions, decoding instructions...\n")
            for content in file_contents:
                print(f"Decoded: {content}\n")
                content_piece = content.split(',')
                self.execute_instruction(content_piece)
                print()


    # Step 3: Instructions are carried out (used inside decode function since each instruction would be exectuted as it is decoded).
    def execute_instruction(self, instruction):
        print(f"Executing instruction...")
        if instruction[0] == 'ADD':
            print(f"Adding values of register indexes {instruction[2]} and {instruction[3]}, and saving to register index {instruction[1]}...")
            registry_address = int(instruction[1][1])
            registry_value = int(self.registers[int(instruction[2][1])]) + int(self.registers[int(instruction[3][1])])
            print("Initiating registry write back...")
            self.registry_write_back(registry_address, registry_value)
        elif instruction[0] == 'ADDI':
            print(f"Adding values of register index {instruction[2]} and immediate {instruction[3]}, and saving to register index {instruction[1]}...")
            registry_address = int(instruction[1][1])
            registry_value = int(self.registers[int(instruction[2][1])]) + int(instruction[3])
            print(f"\nInitiating registry write back...")
            self.registry_write_back(registry_address, registry_value)
        elif instruction[0] == 'J':
            print(f"Executing jump command to location {instruction[1]}...")
            jump_location = int(instruction[1])
            self.counter = jump_location
        elif instruction[0] == 'CACHE':
            cache_action = int(instruction[1])
            if cache_action == 0:
                print("Turning off cache...")
                self.cache.cache_on = False
            elif cache_action == 1:
                print("Turning cache on...")
                self.cache.cache_on = True
            else:
                print("Flushing cache...Don't forget to wash your hands...")
                self.cache.flush_cache
        elif instruction[0] == 'HALT':
            print("Executing halt command, pausing...")
            interrupt_halt = 'nope'
            while interrupt_halt != 'continue':
                interrupt_halt = input(f"If you would like to interrupt the halt command, type 'continue'.\n")
        else:
            print(f"Encountered error while executing, {instruction[0]} is not a known instruction.")

    # Step 4: Retrieves data and adds it to cache via the bus
    def access_memory (self, address, value = None):
        check_bus = self.bus.search_bus(address)
        if check_bus != None:
            print(f"Accessing memory, adding address: {address}, value: {value} to bus...")
            self.bus.add_to_bus(address, value)
            print(f"Bus is delivering data to cache...")
            self.cache.write_cache(address, self.bus.search_bus(address))


    # Step 5: This stage is used if the execution of the instruction impacts data, or existing data is changed or updated
    def registry_write_back (self, address, value):
        self.registers[address] = value
        print()
# CPU provides the instructions and processing power for the computer
# CPU instruction cycle:
    # fetch
    # decode
    # execute
    # memory access
    # registry write-back
# Control Unit (CU): recieves info from software and directs
    # it to relevant harddware components (sends instructions)
# Arithmetic and Logic Unit (ALU): performs arithmetic and logic
    # operations (add/sub, determin equlity, AND/OR/XOR/NOR/NOT/NAND logic)
# Register: volitale memory system that provides CPU w/rapid
    # access to info it is immediatly trying to use
    # stores temp data for immediate processing by ALU
    # hold/flag info if opereation results in overflow/triggers flags
    # hold location of next instruction to be processed by CPU

from cache import Cache
from bus import Bus

class CPU:
    def __init__(self):
        self.cache = Cache()
        self.counter = 0
        pass

    
    def fetch_file_contents(self, file):
        # Program Counter (PC) register stores memory address of the
        # instruction that should be processed next.
        # When time to process the instruction, the CPU copies the 
        # instruction's memory address and stores the copy in another
        # register called the Instruction Register (IR).  Once the memory
        # of the instruction is available, the instruction gets decoded.
        print(f"Fetching {file}...")
        open_file = open(file, 'r')
        file_contents = open_file.readlines()
        for i in file_contents:
            file_contents[file_contents.index(i)] = i.strip()
        return file_contents

    def decode_file_contents(self, file_contents, data_or_instruction):
        # Control Unit deciphers the instruction stored in the IR.
        # As the instruction is decoded it is turned into a series of 
        # control signals used to execute the instruction.
        if data_or_instruction == 'data':
            print("File contains data, decoding data...")
            for content in file_contents:
                print(content)
                content_piece = content.split(',')
                # need to be able to send to 'cpu' to parse instructions, or 
                # to write to memory bus if data...?
                print("Accessing memory, sending content: (address: {content_piece[0]}, value: {content_piece[1]}) to bus...")
                self.access_memory(content_piece)
                pass
        elif data_or_instruction == 'instruction':
            print("File contains instructions, decoding instructions...")
            for content in file_contents:
                print(content)
                content_piece = content.split(',')
                # need to be able to send to 'cpu' to parse instructions, or 
                # to write to memory bus if data...?
                print(f"Executing instruction: {content_piece[0]}...")
                self.execute_instruction(content_piece)
                pass

    # I think needs to happen IN the decode_file_contents method
    def execute_instruction(self, instruction):
        # Instruction is sent to the correct part of the ALU to be
        # processed and completed
        if instruction[0] == "ADD":
            self.execute_add(instruction[1], instruction[2], instruction[3])
        if instruction[0] == "ADDI":
            self.execute_addi(instruction[1], instruction[2], instruction[3])
        if instruction[0] == "J":
            print(f"Executing jump command to location {instruction[1]}...")
            jump_location = int(instruction[1])
            self.counter = jump_location
        if instruction[0] == "CACHE":
            cache_action = instruction[1]
            if cache_action == 0:
                print("Turning off cache...")
                self.cache.cache_on = False
            elif cache_action == 1:
                print("Turning cache on...")
                self.cache.cache_on = True
            else:
                print("Flushing cache...Don't forget to wash your hands...")
                self.cache.flush_cache
        #not sure how to write this next part at this point
        if instruction == 'impacts data':
            self.registry_write_back(instruction)
        pass

    # I believe, if I understand correctly, will access cache before
    # main memory.
    def access_memory (self, something):
        # Retrieve any required data necessary to execute an instruction.
        # This stage only occures if the instruction requires data from memory
        Bus.search_bus(address)
        pass

    def registry_write_back (self, something):
        # This stage only used if the execution of the instruction impacts data.
        # As each instruction is executed data is stored to one of the 
        # registers in the CPU.
        # This stage is also used if existing data is changed or updated
        pass



#------------------------------------------------------------------------
# from cache import Cache
# from bus import Bus

# cpu_count = 0
# num_reg = 9

# #instructions
# inst_add = "ADD"
# inst_addi = "ADDI"
# inst_j = "J"
# inst_cache = "CACHE"

# #values for turning cache on/off/resetting
# cache_off = 0
# cache_on = 1
# cache_clear = 2


# # Helper function to convert register string to index. I.e. register labelled 'R2' should correspond to int index 2
# def convert_register_to_index(value):
#     return int(value[1:])


# # CPU class to implement the bulk of CPU Simulator requirements. Member properties include:
# # CPU Counter - Int representing the number of the instruction being parsed
# # Registers - List used to represent internal registers used by the CPU
# # Cache Flag - boolean representing whether or not the cache is to be used
# # Cache - instance of Cache object instantiated for CPU
# # Memory Bus - instance of Memory Bus object instantiated for CPU
# class CPU:

#     def __init__(self):
#         self.cpu_count = cpu_count
#         self.registers = [0] * num_reg
#         self.cache_flag = False
#         self.cache = Cache()
#         self.memory_bus = Bus()

#     def cpu_count_inc(self):
#         self.cpu_count += 1

#     def reset_cpu_count(self):
#         self.cpu_count = cpu_count

#     def set_cpu_count(self, value):
#         self.cpu_count = value

#     def get_cpu_count(self):
#         return self.cpu_count

#     def reset_registers(self):
#         for i in range(len(self.registers)):
#             self.registers[i] = 0

#     def set_cache_flag(self, value):
#         self.cache_flag = value

#     def clear_cache(self):
#         self.cache.clear_cache()

#     def search_cache(self, address):
#         return self.cache.search_cache(address)

#     def write_cache(self, address, value):
#         self.cache.write_cache(address, value)

#     def search_bus(self, address):
#         return self.memory_bus.search_bus(address)

#     def create_bus(self, address, value):
#         self.memory_bus.create_bus(address, value)

#     # --- Sample implementations for ADD, ADDI, J, and Cache instructions ---

#     def jump_instruction(self, target):
#         self = int(target)

#     def add_instruction(self, destination, source, target):
#         self.registers[convert_register_to_index(destination)] = self.registers[convert_register_to_index(source)] + \
#                                                                  self.registers[convert_register_to_index(target)]

#     def add_i_instruction(self, destination, source, immediate):
#         self.registers[convert_register_to_index(destination)] = self.registers[convert_register_to_index(source)] + \
#                                                                  int(immediate)

#     # Method to implement cache instruction. 0 = OFF, 1 = ON, 2 = Flush Cache
#     def cache_instruction(self, value):
#         if value == cache_off:
#             self.set_cache_flag(False)
#         if value == cache_on:
#             self.set_cache_flag(True)
#         if value == cache_clear:
#             self.flush_cache()

#     # --- Add implementations for further instructions below ---

#     # --------------------------------------------------------- #

#     # Main parser method used to interpret instructions from input file.
#     # Check value of operator and call subsequent helper function
#     def parse_instruction(self, instruction):
#         instruction = instruction.split(",")
#         print("Reading instruction: " + instruction)
#         self.cpu_count_inc()
#         if instruction[0] == inst_add:
#             self.add_instruction(instruction[1], instruction[2], instruction[3])
#         if instruction[0] == inst_addi:
#             self.add_i_instruction(instruction[1], instruction[2], instruction[3])
#         if instruction[0] == inst_j:
#             self.jump_instruction(instruction[1])
#         if instruction[0] == inst_cache:
#             self.cache_instruction(instruction[1])
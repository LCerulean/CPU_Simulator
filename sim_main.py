# Fetch and parse instructions from an input file

# Fetch and parse initialization values for the Memory Bus from a 
# separate input file

# Send CPU instructions and initial Memory Bus values to the CPU and 
# Memory Bus, respectively

# Provide console output to the user documenting the stages of input 
# processing

# Implement an ISA that can handle MIPS Instructions such as the 
# following:
# Instruction	      Operand	         Meaning
# ADD	             Rd, Rs, Rt	      Rd <- Rs + Rt;
# ADDI	            Rt, Rs, immd	  Rt <- Rs + immd
# SUB	             Rd, Rs, Rt       Rd <- Rs - Rt
# SLT	             Rd, Rs, Rt	      If (Rs < Rt) then Rd <- 1 else Rd <- 0
# BNE	           Rs, Rt, offset	  If (Rs not equal Rt) then PC <- (PC + 4) + offset * 4
# J	                  target	      PC <- target * 4
# JAL	              target	      R7 <- PC + 4; PC <- target *4
# LW	           Rt, offset(Rs)	  Rt <- MEM[Rs + offset]
# SW	           Rt, offset(Rs)	  MEM[Rs + offset] <- Rt
# CACHE	                Code	      Code = 0(Cache off) Code = 1(Cache on), Code = 2(Flush cache)
# HALT	                 ;	          Terminate Execution

from cpu import CPU


print("Welcome to the CPU simulator!\nThis simulator will take both instructions and data and use them to simulate the CPU instruction cycle.")
input("Press any key to begin.\n")

cpu_sim = CPU()
print("CPU initialized...")
#fetch instructions and data from files
instruction_file = cpu_sim.fetch_file_contents("instruction_input.txt")
data_file = cpu_sim.fetch_file_contents("data_input.txt")
#decode files, instructions executed as decoded, and data saved to cache
cpu_sim.decode_file_contents(instruction_file, 'instruction')
cpu_sim.decode_file_contents(data_file, 'data')

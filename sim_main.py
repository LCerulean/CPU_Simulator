from cpu import CPU


print("Welcome to the CPU simulator!\nThis simulator will take both instructions and data and use them to simulate the CPU instruction cycle.")
input("Press any key to begin.\n")

cpu_sim = CPU()
print(f"CPU initialized...\n")

#Simulating instruction cycle
instruction_file = cpu_sim.fetch_file_contents("instruction_input.txt")
cpu_sim.decode_file_contents(instruction_file, 'instruction')

print()

#Simulating data storage
data_file = cpu_sim.fetch_file_contents("data_input.txt")
cpu_sim.decode_file_contents(data_file, 'data')

print("Simulation complete!")
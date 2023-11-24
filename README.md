# CPU_Simulator

This project was a portfolio assignment from the Computer Architecture course on Codecademy.  The assignment required that I "research, design, and build a Python program that simulates the functionalities of a CPU."

The assignment was very open-ended as to how and in what way the program simulates a CPU, but did come with two text files to use for testing, one containing data, and the other instructions. After some research I decided to simulate the stages in the __CPU instruction cycle__:  
-Fetch  
-Decode  
-Execute  
-Memory Access  
-Registry Write-Back  

I split the CPU, cache, and (memory) bus into seperate classes and files to represent them as seperate components.  The cache and bus then initialized inside of the CPU class's  _ _ init _ _  method.  Print statements were used throughout the CPU class's methods so that the user would have a visual representation of each stage the program worked through.
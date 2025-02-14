#partC 
# Program Name: Steps Program
# Description: Prints a sequence of steps (1-9) using a single function call with a loop
# Author: Chima
# Date: February 14, 2025

def printSteps(a, b):
   for i in range(a, b + 1):
       print(f"Step {i}")

# Main program
printSteps(1, 9)  # Single function call to print all steps
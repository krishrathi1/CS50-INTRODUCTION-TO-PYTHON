# einstein.py

# Define the speed of light constant in meters per second
c = 300_000_000

# Prompt the user for mass in kilograms
mass = int(input("Enter the mass in kilograms: "))

# Calculate energy using the formula E = mc^2
energy = mass * c ** 2

# Output the equivalent energy in Joules
print(energy)

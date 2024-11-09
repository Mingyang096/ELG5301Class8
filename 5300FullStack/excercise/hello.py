
"""
print('Hello world')

PI = 3.14
PI = 3.15
print(PI)
"""
def calculate_name_length(name):
    # Remove any spaces in the name
    name_without_spaces = name.replace(" ", "")
    
    # Calculate the length of the name
    length = len(name_without_spaces)
    
    return length

# The name to calculate
name = "Mingyang Zhai"

# Calculate and print the length of the name
name_length = calculate_name_length(name)
print(f"The length of the name '{name}' (excluding spaces) is: {name_length}")

def add_numbers_until_stop():
    total_sum = 0
    
    while True:
        user_input = input("Enter a number (or type 'stop' to end): ")
        
        if user_input.lower() == 'stop':
            break
        
        try:
            # Convert input to a float and add to total sum
            number = float(user_input)
            total_sum += number
        except ValueError:
            print("Invalid input. Please enter a valid number or 'stop' to end.")

    return total_sum

# Run the function and print the result
result = add_numbers_until_stop()
print(f"The total sum of the entered numbers is: {result}")

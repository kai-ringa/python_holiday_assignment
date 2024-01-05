# Create a Python script that reads a list of numbers
# Implement functions to find the sum, average, maximum, and minimum of the numbers.
# Implement a function to filter out even numbers from the list.

def read_numbers():
    numbers = []

    while True:
        # Ask user for the list of numbers
        user_input = input('Enter a list of numbers ("or stop to finish"): ')

        # Check of user has finished entering numbers
        if user_input.lower() == 'stop':
            break

        try:
            # Convert input to an integer and add to the numbers list
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print('invalid input. Please enter a valid integer or "stop".')

    return numbers

def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    if not numbers:
        return 0
    
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    if not numbers:
        return None
    
    return max(numbers)

def find_minimum(numbers):
    if not numbers:
        return None
    
    return min(numbers)

def odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

number_list = read_numbers()
print(f'List of numbers: {number_list}')

if number_list:
    print(f'Sum of numbers: {calculate_sum(number_list)}')
    print(f'Average of numbers: {calculate_average(number_list)}')
    print(f'Maximum number in list: {find_maximum(number_list)}')
    print(f'Minimum number in list: {find_minimum(number_list)}')
    print(f'List of odd numbers: {odd_numbers(number_list)}')
else:
    print('No numbers entered')
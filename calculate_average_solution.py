def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

# Additional Test Cases (Optional)
my_numbers2 = [1,2,3,4,5,6,7,8,9,10]
average2 = calculate_average(my_numbers2)
print(f"The average of my_numbers2 is: {average2}")

my_numbers3 = []
average3 = calculate_average(my_numbers3)
print(f"The average of my_numbers3 is: {average3}")

my_numbers4 = [100]
average4 = calculate_average(my_numbers4)
print(f"The average of my_numbers4 is: {average4}")

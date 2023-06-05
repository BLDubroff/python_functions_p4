# Find the maximum of three numbers
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Multiply all numbers in a list
def mult_list(num_list):
    product = 1
    for num in num_list:
        product *= num
    return product

# Reverse a string
def rev_string(string):
    return string[::-1]

# Check if a number is within a given range (inclusive)
def num_within(num, lower_bound, upper_bound):
    return num >= lower_bound and num <= upper_bound


# Print n rows of Pascal's triangle

print('TESTING max_num:')
print(f'(1, 2, 3): {max_num(1, 2, 3)}')
print(f'(3, 2, 1): {max_num(3, 2, 1)}')


print('\nTESTING mult_list:')
print(f'[1, 2, 3, 4]: {mult_list([1, 2, 3, 4])}')
print(f'[]: {mult_list([])}')
print(f'[0, 2, 3, 5]: {mult_list([0, 2, 3, 5])}')

print('\nTESTING rev_string:')
string = 'Hello'
print(f'\'{string}\': {rev_string(string)}')
string = 'Can it reverse longer strings?'

print('\nTESTING num_within:')
print(f'(1, 0, 2): {num_within(1, 0, 2)}')
print(f'(6, 1, 6): {num_within(6, 1, 6)}')



from utill.input_error_handling_utill import input_int_with_constraint


def print_leap_year(year):
    value = False
    if not year % 400:
        value = True
    elif not year % 100:
        value = False
    elif not year % 4:
        value = True
    print(f'{year} is leap: {value}')


print_leap_year(input_int_with_constraint('Please enter year, it should be > 0:\n', 0))

'''           
print_leap_year(1800) #false
print_leap_year(2018) #false
print_leap_year(1917) #false
print_leap_year(2000) #true
print_leap_year(2012) #true
print_leap_year(2244) #true
'''



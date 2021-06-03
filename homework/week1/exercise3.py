#3a
float_var = 8.98
int_var = 4
str_var = 'Jam'

print(f'{float_var}, " ", {int_var}, " ", {str_var}')

#3b
print(f'is_integer method on float: {float_var.is_integer()}')
# returns true is the variable is an integer

print(f'conjugate method on int: {int_var.conjugate()}')
# returns the complex conjugate any any integer

print(f'conjugate method on int: {str_var.swapcase()}') 
# converts the upper case letters to lower case and vice versa
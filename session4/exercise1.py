def Myhellofunction(name):
    print(f"Hello {name}")

Myhellofunction("Jacqueline")
Myhellofunction("Jamal")


#1b 
def check_even(number):
    if number % 2 ==0:
        return True
    else: 
        return False

is_even = check_even(25)
print(is_even)
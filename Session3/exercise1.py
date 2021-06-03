#1a
#price = int(input('Enter the price of the shirt: '))
#if price > 25:
#    print('that is too expensive')

# shirt_price = float(('What is the price the shirt?'))

# #1b
# price = int(input('Enter the price of the shirt: '))
# colour = str(input('What is the colour of the shirt: '))
# if (price >= 25) and (colour == 'blue'):
#     print ("That's perfect")



# #1a
# shirt_price = float(input('What is the price of the shirt?'))
# shirt_in_budget = shirt_price <= 25.00
# print(f'Shirt is available within budget: {shirt_in_budget}')

#1b
shirt_price = float(input('What is the price of the Shirt? '))
shirt_colour = input('What colour is the shirt? ')

shirt_in_budget_and_colour = shirt_price <= 25.00 and shirt_colour == 'blue'
print(f'shirt is available within budget and correct colour: {shirt_in_budget_and_colour}')


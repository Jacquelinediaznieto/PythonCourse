#2a
def shopping_calculator(shopping_cost, discount_applicable):
    if (discount_applicable == 'y'):
        total_cost = shopping_cost * 0.9
        return total_cost
    elif(shopping_cost > 100):
        total_cost = shopping_cost * 0.95  
        return total_cost 
    else:
        total_cost = shopping_cost
        return total_cost


total_cost = shopping_calculator(200, 'y')


print(f'The total cost is  {total_cost}')

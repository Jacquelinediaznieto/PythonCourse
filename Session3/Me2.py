years_of_experience = float(input('How many year of experience do you have?'))
london_based = input('Are you based in London? (y/n)')

can_apply = (years_of_experience > 2) and (london_based == 'y')

print(f'Can you apply fo the job? : {can_apply}')

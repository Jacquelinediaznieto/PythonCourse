#4b
counter = 0 
total_sum = 0
while counter <=500:    
    if(counter % 3 == 0):
        total_sum = total_sum + counter
    counter = counter + 1

print(f'the total sum of all the numbers between 1 and 500 that are multimples of 3 is:{total_sum}')





# with open('d:\Documents\python-course\session7\groceries.txt', 'r') as file: 
#     file_contents = file.read()
#     print((file_contents))

# with open('d:\Documents\python-course\session7\groceries.txt', 'r') as file: 
#     print((file.readline()))  

with open('d:\Documents\python-course\session7\groceries.txt', 'r') as file: 
    line_number = 1
    for myline in (file.readlines()):
        print (f'{line_number} { myline.capitalize() }')
        line_number *= 2
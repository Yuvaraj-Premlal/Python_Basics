# Find the total number of integers from 0 to 99, that doesnt start or end with the number 9

integer_list = list(range(0,100))
print(integer_list)

total_number = 0

for i in integer_list:
    k = str(i)
    nine = "9"
    if nine not in k :
        total_number = total_number+1
print(total_number)

# find the GCD of a number

# method 1

first_number = int(input())
second_number = int(input())

first_number_factors = []
second_number_factors = []

for i in range(1,first_number+1):
    if first_number%i == 0 :
        first_number_factors.append(i)

for i in range(1,second_number+1):
    if second_number%i == 0 :
        second_number_factors.append(i)

gcd = 1

for j in first_number_factors:
    for i in second_number_factors:
        if i ==  j:
            gcd = gcd * i

print("Method 1 | GCD is: " , gcd)

# method 2
def get_rem(max_number,min_number):    
    rem = max_number % min_number
    if rem == 0:
        print("Method 2 | GCD is: ",min_number)
    else:
        get_gcd(rem,max_number,min_number)

def get_gcd(x,max_number,min_number):
        max_number = min_number
        min_number = x
        get_rem(max_number,min_number)

max_number = max(first_number,second_number)
min_number = min(first_number,second_number)

get_rem(max_number,min_number)


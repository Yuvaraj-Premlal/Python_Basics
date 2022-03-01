# Method 1
import time
start_time = time.time()

a = list(range(10))
b = list(range(10))
c = list(range(10))

def square(k):
    return(k*k)


a_square=[]
b_square=[]
c_square=[]

for i in a:
    a_square.append(square(i))

for i in b:
    b_square.append(square(i))

for i in c:
    c_square.append(square(i))

a_square_dict = dict(zip(a,a_square))
b_square_dict = dict(zip(b,b_square))
c_square_dict = dict(zip(c,c_square))

sum_of_squares = 0
for a_key,a_value in a_square_dict.items():
    if a_key > 0:
        for b_key, b_value in b_square_dict.items():
            if b_key > 0:
                sum_of_squares = a_value + b_value
            for c_key,c_value in c_square_dict.items():
                if c_key > 0:
                    if sum_of_squares == c_value:
                        print("The pythagorean_triplets are ",a_key,b_key,c_key)

method_1_time = time.time()-start_time
print("Method 1 : time elapsed %s"%method_1_time)



                        




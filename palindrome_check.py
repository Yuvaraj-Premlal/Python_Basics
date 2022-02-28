a = input("Please enter a string")

# method 1
def palindrome_check(a):
    # string reverse
    a_list = a[::-1]
    if (a == a_list):
        print("Given string is a palindrome")
    else:
        print("Given string is not a palindrome")
palindrome_check(a)

#method 2
print(len(a))
k=''
for i in range(len(a)):
    k += a[-i-1]
print(k)
if k == a:
    print("Method 2: Given string is a palindrome")
else:
    print("Method 2: Given string is NOT a palindrome")
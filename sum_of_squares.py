# Write a program to find the sum of the squares ofall natural numbers from 1 to N
def squaresum(n) :              #define function
    sm = 0                      #initialise sm to zero
    for i in range(1, n+1) :    
        sm = sm + (i * i)       #sm is updating by adding square of no.s
    return sm
n =int(input("enter no"))       #inputing number n
print(squaresum(n))             #printing sum of squares of all natural numbers starting from 1 to n

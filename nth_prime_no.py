n = int(input('Enter : '))                                 #take input to 'n' variale
prime_numbers = [2,3]                                      #create variable 'prime_numbers' and store 2,3 initially
i=3                                                        #create variable 'i' and store 3 initially
if(0<n<3):                                                 #if the value between 1 to 2 operation is performed
    print(n,'th Prime Number is :',prime_numbers[n-1])     #print the list 'prime_numbers' n-1 position value
elif(n>2):                                                 #if value greater than 2 task is performed
    while (True):                                          #create an infinet loop for storing the prime number into the 'prime_numbers'
        i+=1                                               #increase i by one                                        
        status = True                                      #create a boolean variable 'status',initially it is true
        for j in range(2,int(i/2)+1):                      #loop for checking the i number is prime or not prime
            if(i%j==0):                                    #if the reminder of(i/j)is zero,then it is not a prime no.
                status = False                            
                break                                      #and break the loop 'status' will be false
        if(status==True):                                  #if reminder is not zero,'status' is true
            prime_numbers.append(i)                        #then it is stored to 'prime_numbers'
        if(len(prime_numbers)==n):                         #check if the length of list is equal to n valu,then whilw loop will braek
            break
    print(n,'th Prime Number is :', prime_numbers[n-1])    #after braking the loop we print the nth prime number
else:
    print('Please Enter A Valid Number')                   #if user types any wrong or negative value,print 'please enter a valid number'

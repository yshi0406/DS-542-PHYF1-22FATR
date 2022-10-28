#define a zero number to start up
num = 0
#given the range below 1000
for i in range(1,1000): 
    #check multiple of 3 or 5 and sum up
    if i%3==0 or i%5==0: 
        num+=i
#print out the result
print("Sum of all the multiples of 3 or 5 below 1000 is:", num)

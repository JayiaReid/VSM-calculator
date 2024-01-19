#This is a program that calculates the mean, variance and standard deviation of a given data set of positive numbers

#introduction
print("Hi there! Welcome to the Variance and Standard Deviation ft. mean Calculator!\n")
print("=============================================================================\n")

# Get input from user
x = 1
i = 0
list = [] #This is the array that the numbers will be stored

#continuously prompt for numbers until user is finished i.e unbounded loop
while True:
    
    x = float(input("Enter a number or 0 to stop\n"))
    if x==0:
        break
    list.append(x)
    i = i + 1

#removes 0 from the array
list = [num for num in list if num != 0]

#Calculating mean
sum = 0
n = 0
for j in list:
    sum = sum + j #adds numbers while looping through array
    n = n + 1 #keeps count of array elements

mean = sum / n

#Calculating variance (sd^2)
v = 0
for k in list:
    v= v + ((k - mean) ** 2)

variance = v/(n-1)

#standard deviation
import math
sd = math.sqrt(variance) #sd is the standard deviation which is the sqroot of the variance

# Print results
print(f"Mean: {mean:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {sd:.2f}")

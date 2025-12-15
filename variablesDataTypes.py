#Create variables to store your name, age and height
"""
username=input("Enter your name here:")
age=int(input("Enter your age here:"))
height=float(input("Enter your height in metres:"))
while height>4.0:
    print("Kindly enter a realistic height:")
    height=float(input("Re-enter your height here:"))
 
userData=f"Hi there {username}, you are {age} years old and {height} metres tall."
print(userData)
"""

#Write a program that swaps the value of two variables
""""
firstValue=9
secondValue="Nine"
[firstValue,secondValue]=[secondValue,firstValue]
print(f"The first value variable now reads: {firstValue}, while the second value variable now reads {secondValue}")
"""
#Ask the user for two numbers and print their sum, difference, product, and division.
"""
firstDigit=float(input("Enter the value of the first number:"))
secondDigit=float(input("Enter the value of the second number:"))
totalSumResult=firstDigit+secondDigit
differenceResult=firstDigit-secondDigit
productResult=firstDigit*secondDigit
divisionResult=firstDigit/secondDigit
operationData={
    "sum":totalSumResult,
    "difference":differenceResult,
    "product":productResult,
    "division":divisionResult
}
print(operationData)

"""
#Convert a string number (e.g. "25") into an integer and add 10 to it.
"""
currentStringDigit="25"
integerizedDigit=int(currentStringDigit)
additionOperation=integerizedDigit+10
print(additionOperation)
"""
#Check the data type of a variable and print it.
"""
userName="Kevin"
age=22
print(f"The userName is of type {type(userName)} while the age variable is of type {type(age)}")
"""

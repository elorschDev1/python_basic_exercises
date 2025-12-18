
#Write a program that prints the length of a given string.
"""
def findStringLength(testWord):
    return len(testWord)
length=findStringLength("Developer")
print(length)
"""
#Convert a string to all uppercase
"""
def convertStringToUpperCase(convertableString):
    return convertableString.upper()
convertedText=convertStringToUpperCase("cow")
print(convertedText)
"""

#Convert a string to all lowercase
"""
def convertSringToLowerCase(stringToBeConverted):
    return stringToBeConverted.lower()
convertedLowerCaseData=convertSringToLowerCase("BIANCA")
print(convertedLowerCaseData)
"""

#Check if a word is a palindrome.
#I will first reverse the string then join it, and compare it with the original string

def checkIfStringIsPalindrome(stringToCheck):
    reversedString=stringToCheck[::1]
    if stringToCheck == reversedString:
        return "The input string is a palindrome"

    else:
        return "The input string is not a palindrome"
    
testPalindromeResult=checkIfStringIsPalindrome("mm")
print(testPalindromeResult)


#Count how many times a specific character appears in a string.
"""
userName="Bianca"
for letter in userName:
    letterOccurences=userName.count(letter)
    print({
        f"{letter}":f"{letterOccurences}"
    })
    """

#Replace all spaces in a sentence with underscores (_).
"""
currentSentence="This is a python exercise."
underScoreModifiedSentence=currentSentence.replace(" ","_")
print(underScoreModifiedSentence)
"""

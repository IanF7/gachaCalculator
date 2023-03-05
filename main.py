# Ian Fletcher
# Gacha Game Rate Calculator

# imports necessary libraries
import math


# formula used to calculate if something happens at least n times in a binomial distribution
def formula(n, p, r):
    c = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
    return c * math.pow(p, r) * math.pow(1-p, n-r)


cont = ""
while cont != "no":
    # uses inputs to assign values of n, p, and r
    p = float(input("What are the odds of pulling the character once? "))
    # will prompt user to enter a value until the user either enters yes or no
    pulls = int(input("How many pulls will you attempt? "))
    char_per_pull = int(input("How many characters are in each pull attempt? "))
    n = pulls * char_per_pull
    r = int(input("How many times are you wanting to pull the character? "))
    # sets result equal to the formula entered * 100, rounded to the 3rd decimal place
    result = round(formula(n, p, r) * 100, 3)
    # prints results
    print("The odds of pulling this character are " + str(result) + "%")
    # prompts user and asks if user wants to use calculator again
    cont = input("Do you want to calculate the value again? Enter 'yes' if so or 'no' if not: ")
    # will prompt user to enter a value until the user either enters yes or no
    while cont != "yes" and cont != "no":
        cont = input("Please enter a valid option: ")

    print()

#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#
name = input("Please enter your name! \n")
print("Welcomme to Tip calculator, " + name)

total_Bill = float(input("what's your total bill? \n"))

party_size = int(input("How many friends had the share? \n"))

tip_Percentage = int(input("Choose  your top percentage: 10 or 12 or 15? \n"))

final_total = round(
    (total_Bill + (total_Bill * (tip_Percentage / 100))) / party_size, 2)

print("Each person pays ")
print(final_total)

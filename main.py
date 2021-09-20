#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


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

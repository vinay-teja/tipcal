#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#
name = input("Please enter your name! \n")
print("Welcome to Tip calculator!, " + name)

total_Bill = float(input("what's your total bill? \n"))

party_size = int(input("How many friends are sharing this feast ? \n"))

tip_Percentage = int(input("Choose  your top percentage: Example: 10 or 12 or 15? \n"))
# final_total = tip_Percentage /100 *total_Bill + total_Bill
# final_total = total_Bill * (1 + tip_Percentage /100)

final_total = round(
    (total_Bill + (total_Bill * (tip_Percentage / 100))) / party_size, 2)

print(f"Each person pays  {final_total}")

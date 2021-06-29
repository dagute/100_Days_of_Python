#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip Calculator!!")
bill = input("What was the total bill? $")
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))

new_bill = float(bill)
pay_tip = new_bill * (tip / 100)
total = new_bill + pay_tip
total_pay = (total / split)

print("Each Person Should Pay: " + str(round(total_pay, 2)))
